# URLify
# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string. 

import argparse

def replace_space(s):
    return s.replace(' ','%20')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('string', type=str, help='input string')
    args = parser.parse_args()
    res = replace_space(
        args.string
        )
    print(res)

