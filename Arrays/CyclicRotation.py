def solution(A, K):
    """
    Shift array A K times to the right.

    :param A: N Integers
    :param K: rotated K int times
    :return: Shifted Array
    """

    if len(A) == 0:
        return A
    for _ in range(K):
        A.insert(0, A.pop())

    return A

"""
An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given

    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given

    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""


"""
N, K in [0,100]
A within [-1000,1000]


FAILED: Did not account for test cases of K >= N.
Sol: return A[len(A)-K:] + A[:len(A)-K]

The assessment said focus on correctness not performance.

Test cases included:
Empty Array
Single element
Two elements
K < N
K >= N
Small N
Large N
Max N and Max K


L = ['spam', 'Spam', 'SPAM!']
L[2]	 SPAM!	Offsets start at zero
L[-2]	 Spam	Negative: count from the right
L[1:]    ['Spam', 'SPAM!']


Lists are Pythons versions of arrays. So use methods on these lists to act like arrays.
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

"""