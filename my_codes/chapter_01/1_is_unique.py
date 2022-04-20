# 1-1: Is Unique
# Q. Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

import argparse

def is_unique(
    s: str
    ):
    if len(s) == len(set(s)):
        print('All unique!')
        return True
    else:
        print('Not all unique :_(')
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='check if a string has all unique characters or not')
    parser.add_argument('string', type=str, help='input string to check')
    args = parser.parse_args()

    is_unique(
        args.string
    )