with open('/home/fabio/PycharmProjects/Rosalind/datasets/rosalind_bins.txt', 'r') as file:
    n = [int(number) for number in file.readline().split(' ')][0]
    m = [int(number) for number in file.readline().split(' ')][0]
    A = [int(number) for number in file.readline().split(' ')]
    K = [int(number) for number in file.readline().split(' ')]

def binary_search(A, k, low, high):

    print(f"\nNew iteration with low={low} and high={high}")
    if high >= low:
        mid = (high + low) // 2

        if A[mid] == k:
            return mid

        elif k < A[mid]:
            return binary_search(A, k, low, mid - 1)

        else:
            return binary_search(A, k, mid + 1, high)

    else:
        return -1

indices = []
K = [40]

for k in K:
    indices.append(binary_search([10, 20, 30, 40, 50], k, 0, 5))

print(*indices)
