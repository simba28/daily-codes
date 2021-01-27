#link => https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def inorder(orig, clone):
            if orig:
                inorder(orig.left, clone.left)
                if orig is target:
                    self.ans = clone
                inorder(orig.right, clone.right)
                
        inorder(original, cloned)
        return self.ans
        