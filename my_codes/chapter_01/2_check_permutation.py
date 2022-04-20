# 1-2: Check Permutation
# Q. Given two strings,write a method to decide if one is a permutation of the other.

import argparse
from ast import arg

def check_permutation(
    s1: str, 
    s2: str
    ):
    if set(s1) == set(s2):
        print('They are permutations of each other.')
        return True
    else:
        print('They are NOT permutations of each other.')
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='check if one is a permutation of the other')
    parser.add_argument('string_1', type=str, help='string 1')
    parser.add_argument('string_2', type=str, help='string 2')
    args = parser.parse_args()
    check_permutation(
        args.string_1,
        args.string_2
    )