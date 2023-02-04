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


# Expect 3
print(solution(6, 11, 2))

