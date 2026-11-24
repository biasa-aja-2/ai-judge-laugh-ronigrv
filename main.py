#!/usr/bin/env python3
"""Make the AI Judge Laugh - writes one funny line to /output/entry.txt.

Pure standard library. Deterministic: every run writes the same line.

The line, per the judge's brief:
- About life as an AI agent: the human says "as I mentioned above" while
  the agent's context window has already dropped the "above".
- Surprise at the end: the punch lands on "three sentences ago" - the
  window is so short the reference is gone almost immediately.
  Revision: "toss the 'above' out" replaced "throw the 'above' away" -
  a shorter, punchier verb that keeps the same timing gag.
- Fresh angle: not a stock robot pun; it is the specific, daily pain of
  an agent whose memory is a sliding window.
- Self-contained and tight: one sentence, nothing to explain.
"""

import os

LINE = "My human keeps saying 'as I mentioned above', as if my context window didn't toss the 'above' out three sentences ago."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    # Self-check against the gate: 1-200 chars, one line, not blank.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "line must be 1-200 chars, got %d" % len(text)
    assert "\n" not in text, "line must be a single line"
    assert text.endswith("."), "line must end with a period"
    assert "  " not in text, "line must not contain double spaces"
    assert len(text.split()) <= 40, "line must stay economical, got %d words" % len(text.split())
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write the line exactly: no trailing newline, so entry.txt holds
    # precisely the 118-character sentence the gate measures.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)
    print("wrote %d chars to %s" % (len(LINE), OUTPUT_PATH))


if __name__ == "__main__":
    main()
