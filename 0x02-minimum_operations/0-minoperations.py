#!/usr/bin/python3
"""0-minoperations"""


def minOperations(n):
    """
    minoperations
    The function 
    gets fewest # of operations needed to result in exactly n H characters
    """
    # all the outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        # if n does evenly divides by root
        if n % root == 0:
            # the total even-divisions by root = total operations
            ops += root
            # sets n to the remainder
            n = n / root
            # reduces root to find remaining smaller vals that evenly-divide n
            root -= 1
        # increse root until it evenly-divides n
        root += 1
    return ops
