# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        max_dia = 0
        def dfs(node):
            nonlocal max_dia
            if node is None:
                return 0
            # Calculate how many left child
            left = dfs(node.left) 
            
            # calculate how may right child
            right = dfs(node.right)
            
            # Find max of left and right child for each node. 
            max_dia = max(max_dia, left + right)
            
            return 1 + max(left,right)
        dfs(root)
        return max_dia

        