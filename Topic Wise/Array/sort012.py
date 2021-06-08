# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1


class Solution:
    def sort012(self, arr):

        n = len(arr)
        low = 0
        high = n-1
        mid = 0

        while mid <= high:

            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]
                low += 1
                mid += 1

            elif arr[mid] == 1:
                mid += 1

            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr


print(Solution().sort012([2, 1, 0, 0, 2, 1, 1, 1, 2, 0]))
