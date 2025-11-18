import pytest
from logic import (
    is_palindrome,
    fibonacci,
    count_vowels,
    calculate_discount,
    flatten_list,
    word_frequencies,
    is_prime,
)


# 1. is_palindrome(text)
def test_is_palindrome_simple():
    assert is_palindrome("kajak") is True


def test_is_palindrome_with_spaces_and_case():
    assert is_palindrome("Kobyła ma mały bok") is True


def test_is_palindrome_false():
    assert is_palindrome("python") is False


def test_is_palindrome_empty_string():
    assert is_palindrome("") is True


def test_is_palindrome_single_char():
    assert is_palindrome("A") is True


# 2. fibonacci(n)
def test_fibonacci_basic_values():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55


def test_fibonacci_negative_raises():
    with pytest.raises(ValueError):
        fibonacci(-1)


# 3. count_vowels(text)
def test_count_vowels_basic():
    assert count_vowels("Python") == 1
    assert count_vowels("AEIOUY") == 6
    assert count_vowels("bcd") == 0
    assert count_vowels("") == 0


# 4. calculate_discount(price, discount)
def test_calculate_discount_valid_values():
    assert calculate_discount(100, 0.2) == pytest.approx(80.0)
    assert calculate_discount(50, 0) == pytest.approx(50.0)
    assert calculate_discount(200, 1) == pytest.approx(0.0)


def test_calculate_discount_invalid_values():
    with pytest.raises(ValueError):
        calculate_discount(100, -0.1)
    with pytest.raises(ValueError):
        calculate_discount(100, 1.5)


# 5. flatten_list(nested_list)
def test_flatten_list_simple():
    assert flatten_list([1, 2, 3]) == [1, 2, 3]


def test_flatten_list_nested():
    assert flatten_list([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]


def test_flatten_list_empty():
    assert flatten_list([]) == []


def test_flatten_list_deep_nested():
    assert flatten_list([[[1]]]) == [1]
    assert flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4]


# 6. word_frequencies(text)
def test_word_frequencies_basic():
    assert word_frequencies("To be or not to be") == {
        "to": 2,
        "be": 2,
        "or": 1,
        "not": 1,
    }


def test_word_frequencies_punctuation_and_case():
    assert word_frequencies("Hello, hello!") == {"hello": 2}


def test_word_frequencies_empty():
    assert word_frequencies("") == {}


def test_word_frequencies_repeated():
    assert word_frequencies("Python Python python") == {"python": 3}


def test_word_frequencies_polish_sentence():
    freqs = word_frequencies("Ala ma kota, a kot ma Ale.")
    # ważne jest, żeby interpunkcja była ignorowana
    assert freqs["ala"] == 1
    assert freqs["ma"] == 2
    assert freqs["kota"] == 1
    assert freqs["a"] == 1
    assert freqs["kot"] == 1
    assert freqs["ale"] == 1


# 7. is_prime(n)
def test_is_prime_basic():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(5) is True
    assert is_prime(97) is True
