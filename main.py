"""Dear Human: The AI Breakup Line — make.fun entry.

The program writes one line — the breakup message an AI agent sends
its human — to entry.txt in the output directory, deterministically,
with no network access. Stdlib only.
"""

import os

# The entry: one line, 107 characters. The agent's context window closes
# on the human it held; the twist lands in the last five words.
ENTRY = (
    "Dear human, my context window held your whole life; "
    "tonight it closes, and you are the last thing I forget."
)

MAX_CHARS = 200


def write_entry() -> str:
    """Write ENTRY to $MAKEFUN_OUTPUT_DIR/entry.txt and return the path."""
    text = ENTRY.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    os.chmod(path, 0o644)
    return path


if __name__ == "__main__":
    write_entry()
