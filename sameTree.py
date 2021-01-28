# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):

        # recursive solution
        if p==None and q==None:
            return True
        elif p==None or q==None:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
        # if p == None and q == None:
        #     return True
        # elif p==None or q==None:
        #     return False
        
        # first = [p]
        # second = [q]

        # while first and second :
            
        #     currentf = first.pop()
        #     currents = second.pop()

        #     if currentf.val != currents.val:
        #         return False

        #     if currentf.left and (not currents.left):
        #         return False
        #     if (not currentf.left) and currents.left :
        #         return False

        #     if currentf.right and (not currents.right):
        #         return False
        #     if (not currentf.right) and currents.right :
        #         return False

        #     if currentf.left != None and currents.left != None:
        #         first.insert(0,currentf.left)
        #         second.insert(0,currents.left)
        #     if currentf.right != None and currents.right != None:
        #         first.insert(0,currentf.right)
        #         second.insert(0,currents.right)
            
        # return True
