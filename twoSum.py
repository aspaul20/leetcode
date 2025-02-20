class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idx = [(num, i)for i, num in enumerate(nums)]
        nums_idx = sorted(nums_idx, key= lambda x: x[0])
        low = 0 
        high = len(nums)-1
        while low <= high:
            curr = nums_idx[low][0] + nums_idx[high][0]            
            if curr > target:
                high -= 1
            elif curr < target:
                low += 1
            else:
                return [nums_idx[low][1], nums_idx[high][1]]

        
        # mapping = {}

        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if nums[i] not in mapping:
        #         mapping[complement] = i
        #     else:
        #         return [i, mapping[nums[i]]]
          
