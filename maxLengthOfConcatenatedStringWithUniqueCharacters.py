# link => https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

# link => https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/discuss/414172/PythonC%2B%2BJava-Set-Solution


def maxLength(arr):

    dp = [set()]

    for st in arr:

        if len(set(st)) < len(st):
            continue

        st = set(st)
        for c in dp[:]:
            if st & c:
                continue
            dp.append(st | c)

    return max(len(a) for a in dp)
