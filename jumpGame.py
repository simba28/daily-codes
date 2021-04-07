# link => https://leetcode.com/discuss/interview-question/451482/


def dfs(arr, i):

    if i < 0 or i >= len(arr) or arr[i] == -1:
        return False

    if arr[i] == 0:
        return True

    arr[i] = -1
    return dfs(arr, i+arr[i]) or dfs(arr, i-arr[i])


print(dfs([3, 4, 2, 3, 0, 3, 1, 2, 1], 7))
