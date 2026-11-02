"""Small text helpers."""


def word_count(text: str) -> int:
    """Return the number of words in text. Words are separated by whitespace."""
    return len(text.split(" "))


def initials(name: str) -> str:
    """Return the upper-case initials of a name, e.g. "ada lovelace" -> "AL"."""
    return "".join(part[0].upper() for part in name.split())
