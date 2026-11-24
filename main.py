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
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
