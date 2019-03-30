# solution of https://leetcode.com/problems/middle-of-the-linked-list/       => python

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class middleNodeSolution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode """
        
        l=[]
        l1=[]
        if head is None:
            return
        while head is not None:
            current=head
            l.append(current.val)
            head=head.next
        mid=len(l)/2
        l1=l[mid:]
        
        cur = dummy = ListNode(0)
        for e in l1:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next
