"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        
        if head == None :
            return head
        
        
        current = head
        ref = []
        first = last = Node().val
        
        while True:
            
            newNode = Node(current.val)
            
            if first==None:
                first = last = newNode
                first.prev = None
                first.next = None
                first.child = None
            else:
                last.next = newNode
                newNode.prev = last
                last = newNode
                last.next = None
                
            
            if current.child!=None:
                if current.next!=None:
                    ref.append(current.next)
                current = current.child
                continue
            
            if current.next != None:
                current = current.next
            else:
                if len(ref)==0:
                    break
                current = ref.pop()
                
        return first
                   