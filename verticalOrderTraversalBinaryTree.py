# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:

    # solution 1   
    def __init__(self):
        self.min = float('inf')
        self.max = -float('inf')
        self.d = defaultdict(list)
        
    def dfs(self, root, x, y):
        self.min = min(self.min, x)
        self.max = max(self.max, x)
        
        self.d[x].append((y, root.val))
        
        if (root.left):
            self.dfs(root.left, x-1, y+1)
        if (root.right):
            self.dfs(root.right, x+1, y+1)
        
    def verticalTraversal(self, root):
        res = []
        if root == None:
            return res
        
        self.dfs(root, 0, 0)
        
        for i in range(self.min, self.max+1):
            
            tmp = []
            
            for _,k in sorted(self.d[i]):
                tmp.append(k)
            if tmp :
                res.append(tmp)
                
        return res

    '''
    # solution 2
    class Point:
        def __init__(self, x, y, val):
            self.x = x
            self.y = y
            self.val = val
            
    def dfs(self, root, x, y, lst):
        if root == None:
            return
        lst.append(self.Point(x,y,root.val))
        self.dfs(root.left, x-1, y-1, lst)
        self.dfs(root.right, x+1, y-1, lst)
        
        
    def verticalTraversal(self, root):
        res = []
        
        if root == None:
            return res
        
        lst = []
        
        self.dfs(root, 0, 0, lst)
        
        lst.sort(key = lambda i : (i.x, -i.y, i.val))
        
        d = {}
        
        for element in lst:
            
            line = d.get(element.x, [])
            line.append(element.val)
            d[element.x] = line
            
        for i in d.values():
            res.append(i)
        
        return res
    '''