# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def dfs(root, count):
            if not root:
                return None, count

            result, count = dfs(root.left, count)

            if result is not None:
                return result, count 

            count += 1
            if count == k:
                return root.val, count
            
            return dfs(root.right, count)

        result, _ = dfs(root, count)
        return result

        # result = None
        # traversed = 0
        # def dfs(root):

        #     nonlocal result, traversed

        #     if not root or result is not None:
        #         return 

        #     dfs(root.left)
        #     traversed += 1 

        #     if traversed == k: 
        #         result = root.val
        #         return 

        #     dfs(root.right)
        # dfs(root)
        # return result
