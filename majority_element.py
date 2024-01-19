def find_majority(arrays):

    majorities = []

    for array in arrays:
        current_majority = None

        distinct_elements = list(set(array))
        for element in distinct_elements:
            count = array.count(element)

            if count >= len(array) // 2 + 1:
                current_majority = element

        if not current_majority:
            majorities.append(-1)
        else:
            majorities.append(current_majority)

    return majorities

arrays = [[5, 5, 5, 5, 5, 5, 5, 5],
         [8, 7, 7, 7, 1, 7, 3, 7],
         [7, 1, 6, 5, 10, 100, 1000, 1],
         [5, 1, 6, 7, 1, 1, 10, 1]]

print(find_majority(arrays))

