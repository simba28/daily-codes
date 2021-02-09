# link => https://leetcode.com/problems/convert-bst-to-greater-tree/

from treeFromArray import insertLevelOrder, TreeNode


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        if not root:
            return root

        self.largeVal = 0

        def traverse(root):

            if root.right:
                traverse(root.right)

            root.val += self.largeVal
            self.largeVal = root.val

            if root.left:
                traverse(root.left)

        traverse(root)
        return root
