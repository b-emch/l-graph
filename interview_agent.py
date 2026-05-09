#!/usr/bin/env python3
"""
Legacio Discovery — Interview Agent Runner
Simulates stakeholder interviews using persona-grounded AI agents.

Usage:
    python interview_agent.py --persona juriste
    python interview_agent.py --persona dev
    python interview_agent.py --persona ops
    python interview_agent.py --persona juriste --model sonnet
    python interview_agent.py --persona juriste --save
"""

import anthropic
import argparse
import sys
import os
from pathlib import Path
from datetime import datetime

PERSONAS = {
    "juriste": {
        "file": "personas/sophie.md",
        "name": "Sophie",
        "role": "Senior Juriste — Succession Specialist",
        "sentiment": "2/5",
    },
    "dev": {
        "file": "personas/thomas.md",
        "name": "Thomas",
        "role": "Dev Team Lead",
        "sentiment": "4/5",
    },
    "ops": {
        "file": "personas/marc.md",
        "name": "Marc",
        "role": "COO",
        "sentiment": "4/5",
    },
}

MODELS = {
    "haiku": "claude-haiku-4-5-20251001",   # fast, good for live demos
    "sonnet": "claude-sonnet-4-6",           # sharper, better for nuance
}

DIVIDER = "─" * 60


def load_system_prompt(persona_key: str) -> str:
    script_dir = Path(__file__).parent
    persona_path = script_dir / PERSONAS[persona_key]["file"]
    if not persona_path.exists():
        print(f"Error: persona file not found at {persona_path}")
        sys.exit(1)
    return persona_path.read_text(encoding="utf-8")


def print_header(persona: dict, model_label: str) -> None:
    print(f"\n{DIVIDER}")
    print(f"  Legacio Discovery — Interview Simulation")
    print(f"{DIVIDER}")
    print(f"  Persona   : {persona['name']} — {persona['role']}")
    print(f"  Sentiment : {persona['sentiment']} AI adoption score")
    print(f"  Model     : {model_label}")
    print(f"{DIVIDER}")
    print("  Type 'quit' to end  |  'reset' to restart  |  'hint' for probing tips")
    print(f"{DIVIDER}\n")


def print_hints(persona_key: str) -> None:
    hints = {
        "juriste": [
            "Ask about tools she uses day-to-day to surface tool-switching friction.",
            "Ask if she's ever tried an AI tool, even informally — triggers the hidden signal.",
            "Ask 'what happens on a hard day?' to get the deadline stress signal.",
        ],
        "dev": [
            "Ask what they've already tried — surfaces the RAG experiment and its failure.",
            "Ask about compliance or legal walls specifically — triggers the hidden signal.",
            "Ask about document formats to get the OCR quality problem.",
        ],
        "ops": [
            "Ask about second-order costs or what happens if the trajectory continues — triggers attrition signal.",
            "Ask what the previous initiative lacked to surface the 'no baseline metrics' gap.",
            "Push back on his pushback — he respects a PM who doesn't fold under pressure.",
        ],
    }
    print(f"\n  Probing tips for this persona:")
    for tip in hints[persona_key]:
        print(f"  · {tip}")
    print()


def run_interview(persona_key: str, model_key: str, save_transcript: bool) -> None:
    persona = PERSONAS[persona_key]
    model_id = MODELS[model_key]
    system_prompt = load_system_prompt(persona_key)

    client = anthropic.Anthropic()
    messages = []
    transcript_lines = []

    print_header(persona, model_key)

    session_start = datetime.now().strftime("%Y-%m-%d %H:%M")
    transcript_lines.append(f"# Interview Transcript — {persona['name']} ({persona['role']})")
    transcript_lines.append(f"Date: {session_start}  |  Model: {model_key}\n")

    while True:
        try:
            raw = input("Interviewer > ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n  Interview ended.")
            break

        if not raw:
            continue

        if raw.lower() in ("quit", "exit", "q"):
            print("\n  Interview ended.")
            break

        if raw.lower() == "reset":
            messages = []
            transcript_lines.append("\n--- [Session reset] ---\n")
            print(f"\n  Conversation reset. {persona['name']} has no memory of this exchange.\n")
            continue

        if raw.lower() == "hint":
            print_hints(persona_key)
            continue

        messages.append({"role": "user", "content": raw})
        transcript_lines.append(f"**Interviewer:** {raw}")

        try:
            response = client.messages.create(
                model=model_id,
                max_tokens=512,
                system=system_prompt,
                messages=messages,
            )
        except anthropic.APIError as e:
            print(f"\n  API error: {e}\n")
            messages.pop()
            continue

        reply = response.content[0].text
        messages.append({"role": "assistant", "content": reply})
        transcript_lines.append(f"\n**{persona['name']}:** {reply}\n")

        print(f"\n{persona['name']} > {reply}\n")

    if save_transcript and transcript_lines:
        ts = datetime.now().strftime("%Y%m%d_%H%M")
        out_path = Path(__file__).parent / f"transcript_{persona_key}_{ts}.md"
        out_path.write_text("\n".join(transcript_lines), encoding="utf-8")
        print(f"\n  Transcript saved to {out_path.name}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Legacio Discovery — Interview Agent Runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Personas:
  juriste   Sophie — Senior Juriste, Succession Specialist  (AI sentiment 2/5)
  dev       Thomas — Dev Team Lead                          (AI sentiment 4/5)
  ops       Marc   — COO                                    (AI sentiment 4/5)

Examples:
  python interview_agent.py --persona juriste
  python interview_agent.py --persona dev --model sonnet
  python interview_agent.py --persona ops --save
        """,
    )
    parser.add_argument(
        "--persona",
        choices=["juriste", "dev", "ops"],
        required=True,
        help="Which persona to interview",
    )
    parser.add_argument(
        "--model",
        choices=["haiku", "sonnet"],
        default="haiku",
        help="Model to use — haiku (fast, default) or sonnet (sharper)",
    )
    parser.add_argument(
        "--save",
        action="store_true",
        help="Save the interview transcript as a markdown file",
    )

    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        print("Run: export ANTHROPIC_API_KEY=your_key_here")
        sys.exit(1)

    run_interview(args.persona, args.model, args.save)


if __name__ == "__main__":
    main()
