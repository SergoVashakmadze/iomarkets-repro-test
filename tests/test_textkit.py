from textkit import initials, word_count


def test_word_count_simple():
    assert word_count("one two three") == 3


def test_word_count_multiple_whitespace():
    assert word_count("one  two") == 2
    assert word_count("one\ntwo three") == 3
    assert word_count("one\ttwo") == 2
    assert word_count("") == 0


def test_initials():
    assert initials("ada lovelace") == "AL"
