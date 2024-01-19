from merge_sorted_arrays import recursive_merger

def merge_sort(a):
    n = len(a)

    if n <= 1:
        return a

    left = a[:n//2]
    right = a[n//2:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return recursive_merger(sorted_left, sorted_right)

print(merge_sort([10, 2, 5, 3, 7, 13, 1, 6]))




