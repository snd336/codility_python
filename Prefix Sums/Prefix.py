def prefix_summation(a):
    p_sum = [0]
    for i in a:
        p_sum.append(p_sum[-1] + i)  # p_sum[-1] is the last element in the list
    return p_sum


if __name__ == "__main__":

    A = [1, 6, 4, 2, 5, 3]
    N = len(A)

    P = [2]
    Q = [5]
    p = prefix_summation(A)
    print(p)
    for i in range(len(Q)):
        l, r = P[i], Q[i]
        print(p[r] - p[l-1])

