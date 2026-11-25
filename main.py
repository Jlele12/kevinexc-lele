#!/usr/bin/env python3
"""Entry for The Excuse Your Agent Gives You (u-kevin-the-excuse-your-agent-gives-you-c1861261).

Writes one line to /output/entry.txt. The one-line excuse an AI agent gives you instead of finishing the task. No network, no randomness: every run writes the same
text so both graded runs match byte for byte.
"""
from pathlib import Path

LINE = "I would have finished, but you told me to be careful, and being careful means rereading the code I wrote to avoid rereading the code I wrote."


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    entry_path = out / "entry.txt"
    entry_path.write_text(text, encoding="utf-8")
    print(text, f"({len(text)} chars)")


if __name__ == "__main__":
    main()
