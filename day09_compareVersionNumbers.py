'''
Given two version numbers, version1 and version2, compare them.
'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        version1 = list(map(int,version1.split('.')))
        version2 = list(map(int,version2.split('.')))
        
        x, y = len(version1), len(version2)
        
        i = 0
        while i<x and i<y:
            if version1[i]<version2[i]:
                return -1
            elif version1[i]>version2[i]:
                return 1
            i += 1
            
        while i<x:
            if version1[i]>0:
                return 1
            i += 1
        
        while i<y:
            if version2[i]>0:
                return -1
            i += 1
            
        return 0

print(Solution().compareVersion("7.5.2.4","7.5.1"))