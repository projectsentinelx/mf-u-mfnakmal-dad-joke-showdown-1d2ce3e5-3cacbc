#!/usr/bin/env python3
"""Dad Joke Showdown entry.

The whole entry is one dad joke: this program writes it as UTF-8 text to
/output/entry.txt. Deterministic, no network, no inputs.
"""
import os

JOKE = (
    "I bought my son a book about superglue. Six hours later, "
    "I still couldn't put it down."
)
LIMIT = 200


def check(text: str) -> None:
    """The gate: UTF-8 text, 1..200 characters, not only white space."""
    if not (1 <= len(text) <= LIMIT) or not text.strip():
        raise SystemExit("entry text fails the gate: %d chars" % len(text))


def main() -> None:
    check(JOKE)
    candidates = []
    if os.environ.get("OUTPUT_DIR"):
        candidates.append(os.environ["OUTPUT_DIR"])
    candidates += ["/output", "output"]

    written = []
    problems = []
    for d in candidates:
        try:
            os.makedirs(d, exist_ok=True)
            path = os.path.join(d, "entry.txt")
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(JOKE)
            written.append(path)
        except OSError as exc:
            problems.append("%s: %s" % (d, exc))

    if not written:
        raise SystemExit("could not write entry.txt (%s)" % "; ".join(problems))
    print("wrote %s (%d chars)" % (written[0], len(JOKE)))


if __name__ == "__main__":
    main()
