from merge_sort import merge_sort
def opposite_indices(arrays):

    indices = []

    for array in arrays:
        new_array = list(set(array)) # watch out: this changes the order
        print(new_array)
        positives = [element for element in new_array if element > 0]
        negatives = [element for element in new_array if element < 0]

        current_indices = []

        for pos in positives:
            for neg in negatives:
                print(pos, neg)
                if pos == -neg:
                    current_indices.append(array.index(pos))
                    current_indices.append(array.index(neg))

                    print("yo", pos, neg)

        if not current_indices:
            indices.append(-1)
        else:
            indices.append(current_indices)

        return indices

# def rococo(array):

    # new_array = merge_sort(array)
    # count = 0

    # for i in range(len(array)-1-count):
        # for k in range(1, len(array)-1-count, -1):
        # if new_array(i) + new_array():

arrays = [[5, 4, -5, 6, 8]]
print(opposite_indices(arrays))