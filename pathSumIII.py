# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, sum):
        
        def pathSum_helper(root, sum):
            
            if root == None:
                return 0
            res = 0
            if root.val == sum :
                res += 1
            res += pathSum_helper(root.left, sum-root.val)
            res += pathSum_helper(root.right, sum-root.val)
            return res
        
        if root==None:
            return 0
        return self.pathSum(root.left,sum)+self.pathSum(root.right,sum)+pathSum_helper(root, sum)