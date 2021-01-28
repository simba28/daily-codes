'''
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf 
path represents a binary number starting with the most significant bit.  
For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 
01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from 
the root to that leaf.

Return the sum of these numbers.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.res = 0
        print(root)
        
        if root==None:
            return 0
        
        self.traverse(root, str(root.val))
        
        return self.res
    
    def traverse(self, node, no):
        
        if node.left:
            self.traverse(node.left, no+str(node.left.val))
        if node.right: 
            self.traverse(node.right, no+str(node.right.val))
            
        if node.left== None and node.right==None:
            self.res += int(no,2)
        