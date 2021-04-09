# link => https://leetcode.com/problems/group-anagrams/

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []

        present = set()
        idx = 0
        cacheToIdx = {}
        for word in strs:

            sortWord = ''.join(sorted(word))

            if (sortWord in present):
                reqIdx = cacheToIdx[sortWord]
                res[reqIdx].append(word)
            else:
                present.add(sortWord)
                cacheToIdx[sortWord] = idx
                res.append([word])
                idx += 1

        return res


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
