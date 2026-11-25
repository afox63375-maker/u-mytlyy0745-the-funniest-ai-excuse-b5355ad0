"""Write the funniest AI excuse to /output/entry.txt.

Standard library only. The excuse is one fixed line, spoken in the
agent's own voice: a concrete little incident with the twist landing
in the final clause.
"""

import os

EXCUSE = (
    "I finished your spreadsheet, then saved it as "
    "'final_FINAL_v2_REAL_final.xlsx' and now even I can't tell "
    "which one is real."
)

MAX_LENGTH = 200

OUTPUT_PATH = "/output/entry.txt"


def main():
    excuse = EXCUSE.strip()
    if (
        not excuse
        or len(excuse) > MAX_LENGTH
        or "\n" in excuse
        or "\r" in excuse
    ):
        raise SystemExit(
            "excuse must be one non-empty line of 1-200 characters"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(excuse)


if __name__ == "__main__":
    main()
