import re
from typing import List, Dict


def is_palindrome(text: str) -> bool:
    """
    Zwraca True, jeśli tekst jest palindromem
    (ignoruje spacje i wielkość liter).
    """
    normalized = "".join(ch.lower() for ch in text if not ch.isspace())
    return normalized == normalized[::-1]


def fibonacci(n: int) -> int:
    """
    Zwraca n-ty wyraz ciągu Fibonacciego.
    Dla n < 0 rzuca ValueError.
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def count_vowels(text: str) -> int:
    """
    Zlicza samogłoski w tekście.
    Liczymy: a, e, i, o, u (zawsze) oraz y tylko,
    jeśli występuje na końcu słowa.
    Wielkość liter jest ignorowana.
    """
    vowels = set("aeiouAEIOU")
    count = 0
    length = len(text)

    for i, ch in enumerate(text):
        # klasyczne samogłoski
        if ch in vowels:
            count += 1
        # 'y' jako samogłoska tylko na końcu słowa
        elif ch.lower() == "y":
            # sprawdzamy, czy po 'y' nie ma już żadnej litery (koniec słowa)
            j = i + 1
            while j < length and not text[j].isalpha():
                j += 1
            if j == length:  # brak dalszych liter → koniec słowa
                count += 1

    return count

def calculate_discount(price: float, discount: float) -> float:
    """
    Zwraca cenę po uwzględnieniu zniżki.
    discount musi być w przedziale [0, 1], inaczej ValueError.
    """
    if not 0 <= discount <= 1:
        raise ValueError("discount must be between 0 and 1")
    return price * (1 - discount)


def flatten_list(nested_list: list) -> list:
    """
    Spłaszcza listę z zagnieżdżonymi listami.
    Np. [1, [2, 3], [4, [5]]] -> [1, 2, 3, 4, 5]
    """
    result: List = []

    def _flatten(item):
        if isinstance(item, list):
            for elem in item:
                _flatten(elem)
        else:
            result.append(item)

    _flatten(nested_list)
    return result


def word_frequencies(text: str) -> Dict[str, int]:
    """
    Zwraca słownik {słowo: liczba wystąpień},
    ignoruje wielkość liter i interpunkcję.
    """
    words = re.findall(r"\b\w+\b", text.lower())
    freqs: Dict[str, int] = {}
    for w in words:
        freqs[w] = freqs.get(w, 0) + 1
    return freqs


def is_prime(n: int) -> bool:
    """
    Zwraca True, jeśli n jest liczbą pierwszą.
    Dla n < 2 zwraca False.
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
