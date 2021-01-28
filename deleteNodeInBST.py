# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
root = TreeNode(val= 5, left= TreeNode(val= 3, left= TreeNode(val= 2, left= None, right= None), right= TreeNode(val= 4, left= None, right= None)), right= TreeNode(val= 6, left= None, right= TreeNode(val= 7, left= None, right= None)))

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root==None:
            return root
        
        def findPredecessor(node):
            node = node.left
            while node.right!=None:
                node = node.right
            return node.val
        
        def findSuccessor(node):
            node = node.right
            while node.left != None:
                node = node.left
            return node.val
        
        if key>root.val:
            root.right = self.deleteNode(root.right, key)
        elif key<root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left==None and root.right==None:
                root = None
            elif root.left != None:
                root.val = findPredecessor(root)
                root.left = self.deleteNode(root.left, root.val)
            else:
                root.val = findSuccessor(root)
                root.right = self.deleteNode(root.right, root.val)
                
        return root
        
print(Solution().deleteNode(root, 3))