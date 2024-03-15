def highest_even(li):
    evens = []
    for item in li:

        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even([1., 2, 54, 12, 85, 13, 14]))
