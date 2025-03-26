# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(root, curr_sum, path):
            if not root:
                return 
                
            curr_sum += root.val
            path.append(root.val)

            if not root.left and not root.right and curr_sum == targetSum:
                result.append(path.copy())
            
            dfs(root.left, curr_sum, path)
            dfs(root.right, curr_sum, path)
            path.pop()

        dfs(root, 0, [])
        return result
