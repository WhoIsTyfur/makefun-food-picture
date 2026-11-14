"""food-picture-01 entry: write the committed food photo to /output/entry.png, byte for byte.

The picture is a baseline JPEG (1024x1024); the contest tells PNG and JPEG apart by their first bytes, so the
output keeps the name entry.png. Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
MAX_BYTES = 1048576


def gate_ok(data: bytes) -> bool:
    """Cheap stand-in for the sealed gate: size cap and a whole JPEG or PNG."""
    if len(data) > MAX_BYTES:
        return False
    if data[:3] == b"\xff\xd8\xff":
        return data[-2:] == b"\xff\xd9"
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return data[-8:-4] == b"IEND"
    return False


def main() -> int:
    with open(os.path.join(HERE, "food.jpg"), "rb") as f:
        data = f.read()
    if not gate_ok(data):
        print("food.jpg fails the gate checks", file=sys.stderr)
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.png"), "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
