# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def backtrack(root, current_sum, path):
            if not root:
                return 

            current_sum += root.val 
            path.append(root.val)

            if not root.left and not root.right and current_sum == targetSum:
                result.append(path.copy())

            backtrack(root.left, current_sum, path)
            backtrack(root.right, current_sum, path)

            path.pop()
        backtrack(root, 0, [])
        return result

