# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 and not list2:
            return None
        if list1 and list2:
            min_node, max_node = (list1, list2) if list1.val<list2.val else (list2, list1)
            return ListNode(val=min_node.val, next = self.mergeTwoLists(min_node.next, max_node))
        else:
            min_node = list1 if list1 else list2
            return ListNode(val=min_node.val, next = self.mergeTwoLists(min_node.next, None))

        
            