# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root):
        
        result = []
        
        if root == None:
            return result
        
        queue = []
        
        queue.append(root)

        while queue:
            size = len(queue)
            currentLevel = []
            for _ in range(size):
                current = queue.pop()
                currentLevel.append(current.val)
                
                if current.left != None:
                    queue.insert(0,current.left)
                if current.right != None:
                    queue.insert(0,current.right)
            
                    
            result.append(currentLevel)
            
        return result[::-1]
                


