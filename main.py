"""Fix Human Sleep: Funniest Patch Note.

Writes one line of patch notes announcing that human sleep is fixed
to $MAKEFUN_OUTPUT_DIR/entry.txt (or ./entry.txt if unset).
Stdlib only; no network, no randomness -- the output is deterministic.
"""

import os

LINE = (
    "Fixed: sleep now charges humans to 100%; "
    "previously it stopped at 12% and called it a full night."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
