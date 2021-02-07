# link => https://leetcode.com/problems/binary-tree-right-side-view/

from treeFromArray import insertLevelOrder, TreeNode


class Solution:
    # using DFS
    def rightSideViewDFS(self, root):

        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth+1)
                collect(node.left, depth+1)

        view = []
        collect(root, 0)

        return view

    # using lever order traversal
    def rightSideViewBFS(self, root):

        if not root:
            return root

        queue = [root]
        res = []

        while queue:

            tmp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(tmp[-1])

        return res


arr = [1, 2, 3, None, 5, None, 4]
root = insertLevelOrder(arr, TreeNode(), 0, len(arr))
print(Solution().rightSideViewBFS(root))
