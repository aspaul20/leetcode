class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power = []
        current = []

        def build(i):

            if i >= len(nums):
                power.append(current.copy())
                return 
            
            current.append(nums[i])
            build(i+1)

            current.pop()
            build(i+1)

        build(0)
        return power 

        # power = [[], nums]
        # start = 0 

        # while start <= len(nums) - 1:
        #     for i in range(start, len(nums)):
        #         if [nums[i]] not in power:
        #             power.append([nums[i]])
        #         if i != start:
        #             if [nums[start],nums[i]] not in power:
        #                 power.append([nums[start],nums[i]])
        #     start += 1 

        # return power
