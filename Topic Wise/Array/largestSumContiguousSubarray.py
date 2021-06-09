'''
Kadane's Algorithm

Find the sum of contiguous subarray within a one-dimensional array of numbers that has the largest sum.

Algorithm

Initialize:
    max_so_far = INT_MIN
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
  (c) if(max_ending_here < 0)
            max_ending_here = 0
return max_so_far

Time Complexity  O(n)
Space Complexity  O(1)
'''


def maxSubArraySum(lst):
    n = len(lst)

    maxEndingHere = lst[0]
    maxSoFar = -float('inf')

    for element in lst:
        maxEndingHere += element

        if maxEndingHere < 0:
            maxEndingHere = 0

        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere

    return maxSoFar


print(maxSubArraySum([-13, -3, -25, -20, -
                      3, -16, -23, -12, -5, -22, -15, -4, -7]))


# Using DP


def maxSubArraySumDP(a, size):

    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far
