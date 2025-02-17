class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i]-1] :
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1] 

        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
        #     if nums[i] != i: 
        #         nums[i], nums[i-1] = nums[i-1], nums[i]
        # print(nums)
        
        # for i in range(n-1):
        #     if nums[i] == nums[i+1]:
        #         return nums[i] 
        # _max = max(nums)
        # _min = min(nums)
        # __min = min(0, _min)
        # for i in range(__min, _max):
        #     print(i)
        #     if i!=0 and i not in nums:
        #         return i
        # return _max+1
