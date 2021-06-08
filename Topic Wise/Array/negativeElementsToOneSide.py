# https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/


class Solution:
    def rearrange(self, arr):

        n = len(arr)
        left = 0
        right = n-1

        while left <= right:

            if arr[left] < 0 and arr[right] < 0:
                left += 1

            elif arr[left] > 0 and arr[right] < 0:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

            elif arr[left] > 0 and arr[right] > 0:
                right -= 1

            else:
                left += 1
                right -= 1

        return arr


print(Solution().rearrange([-12, 11, -13, -5, 6, -7, 5, -3, 11]))
