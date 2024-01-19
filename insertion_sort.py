def insertion_sort(A):
    count_swaps = 0
    n = len(A)

    for j in range(2, n):
        for k in range(j, 0, -1):
            if A[k] < A[k - 1]:  # > if you want it decreasing
                A[k], A[k - 1] = A[k - 1], A[k]
                count_swaps += 1

    return A, count_swaps

A = [6, 10, 4, 5, 1, 2]
print(insertion_sort(A)[1])



