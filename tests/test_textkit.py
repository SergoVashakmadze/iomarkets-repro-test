from textkit import initials, word_count


def test_word_count_simple():
    assert word_count("one two three") == 3


def test_initials():
    assert initials("ada lovelace") == "AL"
