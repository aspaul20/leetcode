# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        upper_bound = float('inf')
        lower_bound = float('-inf')

        def traverse(root, upper_bound, lower_bound):
            if not root:
                return True
            
            if root.val > lower_bound and root.val < upper_bound:
                return traverse(root.left, root.val, lower_bound) and traverse(root.right, upper_bound, root.val)
            else:
                return False

        return traverse(root, upper_bound,lower_bound)

        # def dfs(root):
            
        #     if not root.left or not root.right:
        #         return True
            
        #     left = dfs(root.left)
        #     right = dfs(root.right)

        #     if root.left.val >= root.val or root.right.val <= root.val:
        #         return False 
        
        #     return True 
        # ret = dfs(root)
        # return ret
