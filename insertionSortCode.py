def insertionSortRecursive(arr, n):

    if n == 1:
        return

    insertionSortRecursive(arr, n-1)

    last = arr[n-1]
    j = n-2
    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = last


def insertionSortIterative(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [12, 11, 13, 5, 6]
# insertionSortRecursive(arr, len(arr))
insertionSortIterative(arr)
print(arr)
