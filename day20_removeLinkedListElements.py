# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head, val):
        
        if head == None:
            return head

        temp = head 
        while temp != None:
            
            if temp.val == val:
                if temp == head:
                    head = head.next
                    temp = head
                else:
                    prev.next = temp.next
                    temp = temp.next
            else:
                prev = temp
                temp = temp.next
                
        return head
                