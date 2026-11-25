"""Worst AI Advice: The 48-Hour Tight Line Open (v2).

Writes one line of the worst possible advice an AI could give to
/output/entry.txt. One line, 140 characters or fewer.
"""

import os

LINE = (
    "As an AI, I recommend microwaving your phone for 30 seconds "
    "to fast-charge it \u2014 the smell means it\u2019s working."
)


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
