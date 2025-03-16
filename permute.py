class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def build(start):
            if start >= len(nums):

                permutations.append(nums.copy())
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                build(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
                
        build(0)
        return permutations 

            
