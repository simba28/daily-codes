# link => https://leetcode.com/problems/count-good-nodes-in-binary-tree/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def helper(node, max_):

            if node.val >= max_:
                self.ans += 1

            if node.left:
                helper(node.left, max(max_, node.val))

            if node.right:
                helper(node.right, max(max_, node.val))

        self.ans = 0
        helper(root, root.val)
        return self.ans
