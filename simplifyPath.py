# link => https://leetcode.com/problems/simplify-path/

import re


class Solution:
    def simplifyPath(self, path: str) -> str:

        path = re.split("/+", path)[1:]

        if path[-1] == '':
            path = path[:-1]

        res = []
        for file in path:

            if file == '.':
                continue

            elif file == '..':
                if len(res) == 0:
                    continue
                res.pop()

            else:
                res.append(file)

        return '/'+'/'.join(res)


print(Solution().simplifyPath("/a/./b/../../c/"))
