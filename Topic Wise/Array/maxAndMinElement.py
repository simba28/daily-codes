# Find Maximum and Minumum Element in Array.


def minMax(lst):
    min_ = float('inf')
    max_ = -float('inf')

    for element in lst:
        max_ = max(element, max_)
        min_ = min(element, min_)

    return (min_, max_)


print(minMax([1, 2, 3, 4, 5]))
