# link => https://leetcode.com/problems/ways-to-make-a-fair-array/

"""
We will split the array into two parts, left and right.
Firstly we count the sum to an array right,
where right[0] = A[0] + A[2] +...
and right[1] = A[1] + A[3] +...

Now we iterate the whole array A, and try to split at each A[i].
When move one element from right to left,
we reduce the sum in right,
check the if it's fair,
then increse the sum in left.


Complexity
Time O(N)
Space O(1)
"""


def waysToMakeFair(A):
    s1, s2 = [0, 0], [sum(A[0::2]), sum(A[1::2])]
    res = 0
    for i, a in enumerate(A):
        s2[i % 2] -= a
        res += s1[0] + s2[1] == s1[1] + s2[0]
        s1[i % 2] += a
    return res
