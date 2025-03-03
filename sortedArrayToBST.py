# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def make_tree(left, right):
            if left > right:
                return 
            mid = (left+right) // 2
            return TreeNode(nums[mid], left=make_tree(left, mid-1), right = make_tree(mid+1, right))
        return make_tree(0, len(nums)-1)
        # def make_tree(nums):
        #     if not nums:
        #         return
        #     mid_idx = len(nums) // 2
        #     print(nums, mid_idx)
        #     mid = TreeNode(nums[mid_idx])
        #     mid.left = make_tree(nums[:mid_idx])
        #     mid.right = make_tree(nums[mid_idx+1:])
        #     return mid 
        # return make_tree(nums)
