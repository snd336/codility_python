# O(N) or O(N*log(N)) Complexity
def solution(A):
    """
    Given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A

    :param A: Array of N integers
    :return: The smallest positive number not in A
    """
    A = list(set(A))
    B = list()
    for i in A:
        if i > 0:
            B.append(i)

    if B:
        B.sort()
    else:
        return 1

    if B[0] != 1:
        return 1

    for i in range(1, len(B)):
        if (B[i - 1] + 1) != B[i]:
            return i + 1

    return len(B) + 1


"""
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""
