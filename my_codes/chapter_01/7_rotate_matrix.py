# Rotate Matrix
# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. 
# Can you do this in place?

'''
Notes
* collects all the positional arguments in a tuple.
** collects all the keyword arguments in a dictionary.
'''

import unittest

def rotate_matrix(m):
    return [list(reversed(row)) for row in zip(*m)]

class Test(unittest.TestCase):
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]
    testable_functions = [
        rotate_matrix
    ]
    def test_functions(self):
        for f in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                assert f(test_matrix) == expected


if __name__ == '__main__':
    unittest.main()