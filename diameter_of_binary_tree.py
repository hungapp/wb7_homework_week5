# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 1
        def cal_depth(node):
            if not node:
                return 0
            l = cal_depth(node.left)
            r = cal_depth(node.right)
            self.diameter = max(self.diameter, l + r + 1)    
            return max(l, r) + 1
        
        cal_depth(root)
        return self.diameter - 1
