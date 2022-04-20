# String Compression
# Implement a method to perform basic string compression using the counts of repeated characters.

import unittest

def compress_str(s):
    car = ''
    output = ''
    count = 0
    for c in s:
        if car != c:
            if count != 0:
                output += car 
                output += str(count)
            car = c
            count = 1
        elif car == c:
            count += 1
    if count != 0:
        output += car 
        output += str(count)
    return output


class Test(unittest.TestCase):
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "a1b1c1d1e1f1"),
        ("aabb", "a2b2"),
        ("aaa", "a3"),
        ("a", "a1"),
        ("", ""),
    ]
    testable_functions = [
        compress_str
    ]
    def test_functions(self):
        for f in self.testable_functions:
            for [test_string, expected] in self.test_cases:
                assert f(test_string) == expected


if __name__ == '__main__':
    unittest.main()