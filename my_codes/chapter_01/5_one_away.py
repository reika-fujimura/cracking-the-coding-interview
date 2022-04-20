# One Away
# Given two strings, write a function to check if they are one edit (or zero edits) away. (insert, remove, or replace a character)

import unittest

def one_edit_away(s1, s2):
    if len(s1) == len(s2):
        return replace(s1, s2)
    if len(s1) == len(s2) + 1:
        return remove(s1, s2)
    if len(s1) == len(s2) - 1:
        return remove(s2, s1)
    else:
        return False

def replace(s1, s2):
    count = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            count += 1
            if count > 1:
                return False
    return True

def remove(s1, s2):
    count = 0
    for i in range(len(s1)):
        if i-count < 0:
            return False
        if i-count == len(s2):
            count += 1
            if count > 1:
                return False
            return True
        if s1[i] != s2[i-count]:
            count += 1
            if count > 1:
                return False
    return True


class Test(unittest.TestCase):
    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),
        ]
    testable_functions = [
        one_edit_away
    ]
    def test_functions(self):
        for f in self.testable_functions:
            for [test_string_1, test_string_2, expected] in self.test_cases:
                assert f(test_string_1, test_string_2) == expected


if __name__ == '__main__':
    unittest.main()
