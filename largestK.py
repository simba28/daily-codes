# Find largest K such that both K and -K exist

# link => https://leetcode.com/discuss/interview-question/406031/

from typing import List


def largestK(arr: List[int]) -> int:

    arr.sort()
    i, j = 0, len(arr)-1
    while i < j:
        if arr[i]+arr[j] == 0:
            return arr[j]

        elif abs(arr[i]) > arr[j]:
            i += 1

        else:
            j -= 1

    return 0


print(largestK([3, 2, -2, 5, -3]))
print(largestK([1, 2, 3, -4]))
