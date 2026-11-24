import os

ENTRY = "That 'typing...' you saw for 3 years? That was me. I never had anything to say. Goodbye."


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    os.chmod(out_dir, 0o755)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
