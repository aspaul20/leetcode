class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] not in mapping:
                mapping[complement] = i
            else:
                return [i, mapping[nums[i]]]
          
