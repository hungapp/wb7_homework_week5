# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.max_length = 0

        def arrow_length(node, val):
            if not node: return 0
            left_length = arrow_length(node.left, node.val)
            right_length = arrow_length(node.right, node.val)

            self.max_length = max(self.max_length, left_length + right_length)
            if node.val == val:
                return max(left_length, right_length) + 1
            return 0
        if not root: return 0
        arrow_length(root, root.val)
        return self.max_length
