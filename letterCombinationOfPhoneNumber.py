# link => https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:
    def letterCombinations(self, digits: str):

        cache = {'2': ('a', 'b', 'c'), '3': ('d', 'e', 'f'), '4': ('g', 'h', 'i'), '5': ('j', 'k', 'l'),
                 '6': ('m', 'n', 'o'), '7': ('p', 'q', 'r', 's'), '8': ('t', 'u', 'v'),
                 '9': ('w', 'x', 'y', 'z')}

        if digits == "":
            return []

        lst = []

        def helper(tmp, pos):

            if pos >= len(digits):
                lst.append(tmp)
                return

            for ch in cache[digits[pos]]:
                helper(tmp+ch, pos+1)

        helper('', 0)

        return lst
