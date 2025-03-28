# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []

        def dfs(root, current):
            if not root:
                return 
            current += str(root.val)

            if not root.left and not root.right: 
                result.append(int(current))
                # return 

            dfs(root.left, current)
            dfs(root.right, current)

            current = current[:-1]
        dfs(root, '')

        return sum(result)

        
