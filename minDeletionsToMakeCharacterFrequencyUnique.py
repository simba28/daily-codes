# link => https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/


class Solution:
    def minDeletions(self, s: str) -> int:

        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        ans = 0
        seen = set()

        for k in sorted(freq.values(), reverse=True):

            while k in seen:
                k -= 1
                ans += 1

            if k:
                seen.add(k)

        return ans


print(Solution().minDeletions('aaabbbcc'))
