# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if root1 and root2:
            value = root1.val + root2.val
            return TreeNode(value, self.mergeTrees(root1.left, root2.left), self.mergeTrees(root1.right, root2.right))
        elif root1:
            value = root1.val
            return TreeNode(value, self.mergeTrees(root1.left, None), self.mergeTrees(root1.right, None))
        elif root2:
            value = root2.val
            return TreeNode(value, self.mergeTrees(None, root2.left), self.mergeTrees(None, root2.right))
        else:
            return None