import pytest
from string_utils import (
    count_vowels,
    reverse_string,
    is_palindrome,
    word_count,
    capitalise_words,
    remove_duplicates
)

# ---------- count_vowels tests ----------
def test_count_vowels_basic():
    assert count_vowels("Hello") == 2

def test_count_vowels_case_insensitive():
    assert count_vowels("AbCdEfG") == 2  # A, E

def test_count_vowels_empty_string():
    assert count_vowels("") == 0

def test_count_vowels_no_vowels():
    assert count_vowels("xyz") == 0

# ---------- reverse_string tests ----------
def test_reverse_string_basic():
    assert reverse_string("abc") == "cba"

def test_reverse_string_single_char():
    assert reverse_string("a") == "a"

def test_reverse_string_empty():
    assert reverse_string("") == ""

# ---------- is_palindrome tests ----------
def test_is_palindrome_basic():
    assert is_palindrome("racecar") is True

def test_is_palindrome_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") is True

def test_is_palindrome_case_insensitive():
    assert is_palindrome("RaceCar") is True

def test_is_palindrome_not_palindrome():
    assert is_palindrome("hello") is False

def test_is_palindrome_empty_string():
    assert is_palindrome("") is True

# ---------- word_count tests ----------
def test_word_count_basic():
    assert word_count("Hello World") == 2

def test_word_count_multiple_spaces():
    assert word_count("  Hello   World  ") == 2

def test_word_count_empty_string():
    assert word_count("") == 0

def test_word_count_only_spaces():
    assert word_count("   ") == 0

# ---------- capitalise_words tests ----------
def test_capitalise_words_basic():
    assert capitalise_words("hello world") == "Hello World"

def test_capitalise_words_mixed_case():
    assert capitalise_words("hElLo WoRlD") == "Hello World"

def test_capitalise_words_single_word():
    assert capitalise_words("python") == "Python"

def test_capitalise_words_empty():
    assert capitalise_words("") == ""

# ---------- remove_duplicates tests ----------
def test_remove_duplicates_basic():
    assert remove_duplicates("aaabbbcc") == "abc"

def test_remove_duplicates_long_consecutive():
    assert remove_duplicates("aaaabbbbbcccc") == "abc"

def test_remove_duplicates_no_consecutive():
    assert remove_duplicates("abc") == "abc"

def test_remove_duplicates_empty():
    assert remove_duplicates("") == ""

# ---------- Edge cases & exception handling ----------
def test_count_vowels_none_raises_typeerror():
    with pytest.raises(TypeError):
        count_vowels(None)

def test_reverse_string_none_raises_typeerror():
    with pytest.raises(TypeError):
        reverse_string(None)

def test_is_palindrome_none_raises_typeerror():
    with pytest.raises(TypeError):
        is_palindrome(None)

def test_word_count_none_raises_typeerror():
    with pytest.raises(TypeError):
        word_count(None)

def test_capitalise_words_none_raises_typeerror():
    with pytest.raises(TypeError):
        capitalise_words(None)

def test_remove_duplicates_none_raises_typeerror():
    with pytest.raises(TypeError):
        remove_duplicates(None)