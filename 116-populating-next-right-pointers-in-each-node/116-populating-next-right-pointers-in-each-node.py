"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root:
            self.connect_2(root.left, root.right)
        return root
    
    def connect_2(self,l,r):
        # print(l.val, r.val)
        if l and r:
            if l.left:
                self.connect_2(l.left,l.right)
                self.connect_2(l.right, r.left)            
                self.connect_2(r.left,r.right)     
            l.next = r