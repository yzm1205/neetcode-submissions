# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
            
        output = []
        que_lvl = deque([(root,1)])
        def inorder(node):
            if not node:
                return 0
            while que_lvl:
                node,lvl = que_lvl.popleft()
                if len(output) < lvl:
                    output.append([node.val])
                else:
                    output[lvl-1].append(node.val)
                # print(f"{output=}")
                if node.left:
                    que_lvl.append((node.left,lvl+1))
                if node.right:
                    que_lvl.append((node.right,lvl+1))
        inorder(root)
        return output
