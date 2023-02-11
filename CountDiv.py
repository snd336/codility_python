# O(1) Complexity
def solution(A, B, K):
    """
    A function that computer all i s.t. { i : A ≤ i ≤ B, i mod K = 0 }.

    :param int A: Within [0..2,000,000,000]
    :param int B: Within [0..2,000,000,000]
    :param int K: Within  [1..2,000,000,000]
    :return int: Number of integers within [A:B] that are divisible by K
    """
    # // gives the next whole number to left on the number line
    high_limit = (B//K)
    # negating and turning back positive gives whole number to right
    low_limit = -(-A//K)

    # high - low is effectively reducing all divisible numbers by K
    # so count the number if factors
    return high_limit - low_limit + 1


"""
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
"""

