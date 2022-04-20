# Palindrome Permutation
# Given a string, write a function to check if it is a permutation of a palin­drome.

import unittest
from collections import Counter
import string

def clean_phrase(phrase):
    return [c for c in phrase.lower() if c in string.ascii_lowercase]
    
def is_palindrome_permutation_pythonic(phrase):
    counter = Counter(clean_phrase(phrase))
    return sum(val%2 for val in counter.values()) <= 1


class Test(unittest.TestCase):
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("a-bba!", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]
    testable_functions = [
        is_palindrome_permutation_pythonic,
    ]

    def test_functions(self):
        for f in self.testable_functions:
            for [test_string, expexted] in self.test_cases:
                assert f(test_string) == expexted


if __name__ == '__main__':
    unittest.main()