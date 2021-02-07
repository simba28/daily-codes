# link => https://leetcode.com/problems/linked-list-cycle/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        # using two pointers, slow and fast
        # try catch block reduced the speed by some extent as we are not
        # checking for list end every time
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

        '''
        # two pointer approach

        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
            
        return True
        '''
        '''
        # using dictionary to store the particular nodes
        cache = {}
        
        while head:
            
            if head in cache:
                return True
            cache[head] = True
            head = head.next
            
        return False
        '''
