# link => https://leetcode.com/problems/restore-ip-addresses/

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []

        def generator(fullIp, idx):

            if len(fullIp) == 4:
                if idx == len(s):
                    res.append('.'.join(fullIp))
                return

            for i in range(3):

                if not (idx+i < len(s)):
                    return

                else:

                    part = s[idx: idx+i+1]
                    if 0 <= int(part) <= 255 and len(part) == len(str(int(part))):
                        fullIp.append(part)
                        generator(fullIp, idx+i+1)
                        fullIp.pop()

        generator([], 0)

        return res


print(Solution().restoreIpAddresses("25525511135"))
