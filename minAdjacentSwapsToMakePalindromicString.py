# link => https://leetcode.com/discuss/interview-question/351783/


def isValidPalindrome(s: str) -> bool:

    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    oddCount = 0
    for ch in count:
        if count[ch] % 2 != 0:
            oddCount += 1

    return False if oddCount > 1 else True


def minSwaps(s: str) -> int:
    """
    Time : O(n^2)
    Space : O(n)
    """

    if not isValidPalindrome(s):
        return -1

    s = list(s)

    f, b = 0, len(s)-1
    swaps = 0

    while f < b:

        if s[f] == s[b]:
            f += 1
            b -= 1

        else:

            mid = b
            while mid > f and s[mid] != s[f]:
                mid -= 1

            if mid == f:
                s[mid], s[mid+1] = s[mid+1], s[mid]
                swaps += 1
                continue

            for i in range(mid, b):
                s[i], s[i+1] = s[i+1], s[i]
                swaps += 1

            f += 1
            b -= 1

    return swaps


if __name__ == "__main__":
    print(minSwaps("mamad"))
    print(minSwaps("asflkj"))
    print(minSwaps("aabb"))
    print(minSwaps("ntiin"))
