'''
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) :
        lst1 = self.inOrder(root1, [])
        lst2 = self.inOrder(root2, [])
        
        if lst1 and lst2:
            return self.merge(lst1, lst2)
        if lst1==None:
            return lst2
        if lst2==None:
            return lst1
        
        
    def inOrder(self, node, lst):
        
        if node == None:
            return
        
        self.inOrder(node.left, lst)
        lst.append(node.val)
        self.inOrder(node.right, lst)
        
        return lst
    
    def merge(self, first, sec):
        
        x = len(first)
        y = len(sec)
        
        res = []
        i = 0
        j = 0
        while i<x and j<y:
            if first[i]<sec[j]:
                res.append(first[i])
                i += 1
            else:
                res.append(sec[j])
                j += 1
                
        if i<x:
            res.extend(first[i:])
        if j<y:
            res.extend(sec[j:])
            
        return res