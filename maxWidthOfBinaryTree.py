
# for width in a binary tree, go for level order
# traversal with the position of each node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root) -> int:

        
        maxWidth = 0
        
        if root == None:
            return maxWidth
        
        queue = [[root,0]]
        maxWidth = 1
        
        while len(queue)>0:
            
            size = len(queue)
            start = queue[0][1]
            end = queue[-1][1]
            maxWidth = max(maxWidth, end-start+1)
            for _ in range(size):
                current = queue.pop(0)
                idx = current[1]-start
                
                if current[0].left != None:
                    queue.append([current[0].left,2*idx +1])
                if current[0].right != None:
                    queue.append([current[0].right,2*idx + 2])
            
        return maxWidth