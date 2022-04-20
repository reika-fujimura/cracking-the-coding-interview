# Rotate Matrix
# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. 
# Can you do this in place?

import unittest

def rotate_matrix():
    return None

class Test(unittest.TestCase):
    test_cases = [
    ]
    testable_functions = [
        rotate_matrix
    ]
    def test_functions(self):
        for f in self.testable_functions:
            for [test_string, expected] in self.test_cases:
                assert f(test_string) == expected


if __name__ == '__main__':
    unittest.main()