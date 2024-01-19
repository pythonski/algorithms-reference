def merger(a, b):

    c = []
    count_a = 0
    count_b = 0

    while count_a < len(a) and count_b < len(b):
        if a[count_a] <= b[count_b]:
            c.append(a[count_a])
            count_a += 1

        else:
            c.append(b[count_b])
            count_b += 1

    while count_a < len(a):
        c.append(a[count_a])
        count_a += 1

    while count_b < len(b):
        c.append(b[count_b])
        count_b += 1

    return c

def recursive_merger(a, b):

    if not a:
        return b

    if not b:
        return a

    if a[0] <= b[0]:
        print(type(a))
        return [a[0]] + recursive_merger(a[1:], b)

    else:
        print(type(b))
        return [b[0]] + recursive_merger(a, b[1:])

a = [2, 4, 10, 18]
b = [-5, 11, 12]

print(recursive_merger(a, b))


