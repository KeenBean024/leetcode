# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
#     #RECURSIVE T O(N)  M O(N)
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if head is None:
#             return None
        
#         new_head = head
#         if head.next:
#             new_head = self.reverseList(head.next)
#             head.next.next = head
#             head.next = None
#         return new_head
    
    # ITERATIVE T O(N)  M(1)
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        left = None
        right = head
        while right:
            temp = right.next
            right.next = left
            left=right
            right = temp
        return left