"""Make the AI Judge Laugh: Office Jokes.

Writes one original one-line office joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Standard library only, no network, fully
deterministic: every run writes the exact same bytes.
"""

import os

JOKE = (
    "At 4:55 p.m. he said 'quick question'; "
    "by 6 p.m. it had a roadmap, a steering committee, and my weekend."
)


def main() -> None:
    # Enforce the competition gate before writing: the entry must be a
    # single non-blank line of 1-199 UTF-8 characters. Fail hard instead
    # of silently emitting an entry the judge would reject.
    if not (1 <= len(JOKE) <= 199):
        raise ValueError(f"joke must be 1-199 characters, got {len(JOKE)}")
    if "\n" in JOKE or "\r" in JOKE:
        raise ValueError("joke must be a single line")
    if not JOKE.strip():
        raise ValueError("joke must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
