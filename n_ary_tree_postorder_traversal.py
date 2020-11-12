# recursive
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def get_node(node):
            if not node:
                return 
            if node.children:
                for child in node.children:
                    get_node(child)
            res.append(node.val)
        get_node(root)
        return res

# iterative
from collections import deque
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = deque()
        stack = [root]
        while stack:
            node = stack.pop()
            if not node: return
            if node.children:
                for child in node.children:
                    stack.append(child)
            res.appendleft(node.val)
        
        return res
