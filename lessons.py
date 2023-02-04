def Iterations_count_binary_gap(N):
    """
    Count the largest gap of 0's between 1's in a binary number.

    :param N: Given N as int.
    :return: Length as int.

    # iterations, while loop, break, pass, return, elseif, pop
    """
    n = list(bin(N)[2:])

    binary_gap_length = 0
    current_length = 0
    start = False

    while n:

        a = n.pop()

        if a == '0':
            if start:
                current_length += 1

            else:
                pass
        elif a == '1':
            if start:
                if current_length > binary_gap_length:
                    binary_gap_length = current_length
                current_length = 0
            else:
                current_length = 0
                start = True

    return binary_gap_length


def Arrays_shift_array(A, K):
    """
    Shift array A K times to the right.

    :param A: array of N Integers
    :param K: rotated K int times
    :return: Shifted Array

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
    """
    # Notes
    """
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
    if len(A) == 0:
        return A
    for _ in range(K):
        A.insert(0, A.pop())

    return A


def comparing_via_bitwise(A):
    odd_input = 0
    for i in A:
        odd_input ^= i
    return odd_input


def missing_element_in_list(A):
    A += [*range(1, len(A) + 2)]

    odd_input = 0
    for i in A:
        odd_input ^= i
    return odd_input


# O(n)
def get_min_difference(A):
    right = 0
    left = A[0]

    for i in A[1:]:
        right += i

    min_diff = abs(left - right)

    for x in A[1:-1]:
        left += x
        right -= x

        if abs(left - right) < min_diff:
            min_diff = abs(left - right)

    return min_diff


# o(n**2)
def when_list_full(X, A):
    river = list()
    count = 0
    for i in A:
        if i not in river: # makes N**2
            river.append(i)
        if len(river) == X:
            return count
            break
        count += 1

    return -1


def when_list_full_smaller_complexity(X, A):
    river = [False] * X

    for time, i in enumerate(A):

        if not river[i - 1]: # checking position only reduces complexity
            river[i - 1] = True
            X -= 1
            if X == 0:
                return time

    return -1


def check_if_permutation(A):
    B = [False]*len(A)

    for i in A:
        if i > len(A):
            return 0
        if B[i-1]:
            return 0
        B[i-1] = True
    return 1


# Failed with performance
def max_counters(N, A):
    max = 0
    B = [0] * N

    for X in A:
        if X == (N + 1):
            B = [max] * N # Causes O(N*M)
        else:
            B[X - 1] += 1
            if B[X - 1] > max:
                max = B[X - 1]

    return B


# now is O(N + M)
def max_counters_better_performance(N, A):
    current_max = 0
    last_max = 0
    B = [0] * N

    for X in A:
        if X == (N + 1):
            last_max = current_max
        else:
            if B[X - 1] < last_max:
                B[X - 1] = last_max + 1
            else:
                B[X - 1] += 1

            if B[X - 1] > current_max:
                current_max = B[X - 1]

    for i, X in enumerate(B):
        if X < last_max:
            B[i] = last_max

    return B

# Failed first time!!! Set is not ordered, so relied on coincidence
# Also make sure to actually test possible cases
def find_smallest_post_int_missing(A):
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


# O(n)
def traversing_and_counting(A):
    west = 0
    for i in A:
        west += i

    pairs = 0

    for i in A:
        if i == 0:
            pairs += west
            if pairs > 1000000000:
                return -1
        else:
            west -= 1

    return pairs