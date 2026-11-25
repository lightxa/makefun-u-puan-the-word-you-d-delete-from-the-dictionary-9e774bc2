"""The Word You'd Delete From the Dictionary.

Writes exactly one word to /output/entry.txt: the single word this
entry would erase from the dictionary forever.

The word: lisp.

Why this word: it names a speech impediment, yet it is itself
unpronounceable by the very people it describes. The joke lives in
the word's own sound, needs no caption, and deleting it would remove
the one word that taunts the people it names.
"""

import os

WORD = "lisp"


def _validate(word: str) -> None:
    """Guard the gate ourselves: one real word, 1-77 chars, UTF-8."""
    if not word or len(word) > 77:
        raise ValueError("word fails the gate length")
    if word != word.strip() or " " in word or "\n" in word:
        raise ValueError("entry must be exactly one word")
    word.encode("utf-8")


def main() -> None:
    _validate(WORD)
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
