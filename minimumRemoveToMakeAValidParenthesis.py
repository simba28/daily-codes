# link => https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        s = list(s)
        stack = []

        for i, ch in enumerate(s):

            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop(-1)
                else:
                    s[i] = ''

        while stack:
            s[stack.pop()] = ''

        return ''.join(s)


print(Solution().minRemoveToMakeValid("a)b(c)d"))
