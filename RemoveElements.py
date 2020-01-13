# solution of https://leetcode.com/problems/remove-linked-list-elements/

# dummy_head
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head
        node = dummy_head
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return dummy_head.next


# Recursive solution===================================================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None: return None
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            return head.next
        return head
                
                
                
                
        
