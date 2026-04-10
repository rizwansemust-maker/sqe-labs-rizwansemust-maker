def count_vowels(text: str) -> int:
    """Return the count of vowels (a, e, i, o, u) case-insensitively."""
    if text is None:
        raise TypeError("Input cannot be None")
    vowels = set('aeiou')
    return sum(1 for ch in text.lower() if ch in vowels)


def reverse_string(text: str) -> str:
    """Return the reversed string."""
    if text is None:
        raise TypeError("Input cannot be None")
    return text[::-1]


def is_palindrome(text: str) -> bool:
    """Return True if text reads same forwards/backwards (case-insensitive, ignoring spaces)."""
    if text is None:
        raise TypeError("Input cannot be None")
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def word_count(text: str) -> int:
    """Return number of words separated by whitespace."""
    if text is None:
        raise TypeError("Input cannot be None")
    if not text.strip():  # empty or only spaces
        return 0
    return len(text.split())


def capitalise_words(text: str) -> str:
    """Return text with first letter of each word capitalised, rest lowercased."""
    if text is None:
        raise TypeError("Input cannot be None")
    return ' '.join(word.capitalize() for word in text.split())


def remove_duplicates(text: str) -> str:
    """Remove consecutive duplicate characters, preserve first occurrence."""
    if text is None:
        raise TypeError("Input cannot be None")
    if not text:
        return ""
    result = [text[0]]
    for ch in text[1:]:
        if ch != result[-1]:
            result.append(ch)
    return ''.join(result)