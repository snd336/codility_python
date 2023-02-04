


def solutions(A):
    d1 = {}
    d2 = {}
    for i in range(1, len(A), 2):
        print(i)
        if (A[i-1] + A[i]) in d1:
            d1[A[i-1] + A[i]] += 1
        else:
            d1[A[i-1] + A[i]] = 1

    for i in range(1, len(A) - 1, 2):

        if (A[i] + A[i+1]) in d2:
            d2[A[i] + A[i+1]] += 1
        else:
            d2[A[i] + A[i + 1]] = 1


    return max(len(d1), len(d2))

solutions([10,1,3,1,2,2,1,0,4])


