import os

TEXT = "I asked my agent for a one-line fix; it rewrote 47 files, added a test suite, a README, and a changelog, then proudly announced the bug was still there — but the bug is now beautifully documented."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
