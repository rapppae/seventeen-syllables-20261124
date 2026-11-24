"""Write the 17-syllable debugging haiku to /output/entry.txt."""

from pathlib import Path

# 5-7-5 haiku, 17 syllables; two newlines, no trailing newline.
ENTRY = (
    "breakpoint holds its breath\n"
    "the stack trace blames my own line\n"
    "it was a typo"
)

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
