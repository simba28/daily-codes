# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree_rec(self, i1, i2, p1, p2):
        
        if i1 >= i2 or p1 >= p2: return None
        root = TreeNode(self.postorder[p2-1])
        # it = self.inorder.index(self.postorder[p2-1])
        it = self.d[self.postorder[p2-1]]
        diff = it - i1
        root.left = self.buildTree_rec(i1, i1+diff, p1, p1 + diff)
        root.right = self.buildTree_rec(i1+diff+1, i2, p1+diff, p2-1)
        
        return root

    def buildTree(self, inorder, postorder):
        
        n = len(inorder)
        if n==0: return None
        
        self.d = {}
        for i in range(len(inorder)):
            self.d[inorder[i]] = i
            
        self.inorder = inorder
        self.postorder = postorder
        return self.buildTree_rec(0, n, 0, n)

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
            
        return result

print(Solution().levelOrderBottom(Solution().buildTree([9,3,15,20,7],[9,15,7,20,3])))
        