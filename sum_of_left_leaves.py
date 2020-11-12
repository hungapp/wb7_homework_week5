# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.total = 0
        def sum_left(node, is_left = False):
            if not node:
                return 
            sum_left(node.left, True)
            if not node.left and not node.right and is_left:
                self.total += node.val
            sum_left(node.right)
        sum_left(root)
        return self.total
            
