# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root):
        self.res = 0
        self.helper(root)
        
        return self.res
        
    def helper(self, node):
        if node == None:
            return
        
        if node.left:
            if not node.left.left and not node.left.right:
                self.res += node.left.val
            self.helper(node.left)

        if node.right:
            self.helper(node.right)