class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = 0 
        end = len(nums) - 1
        red_count = 0
        while curr <= end:
            if nums[curr] == 2:
                nums[curr], nums[end]= nums[end], nums[curr]
                end -= 1
                red_count += 1
            else:
                curr += 1
        curr = 0 
        end = len(nums)-red_count-1
        while curr <= end: 
            if nums[curr] == 1:
                nums[curr], nums[end]= nums[end], nums[curr]
                end -= 1
            else:
                curr += 1
        # from collections import Counter
        # num_count = Counter(nums)
        # nums[0:num_count[0]] = num_count[0]*[0]
        # nums[num_count[0]:num_count[0]+num_count[1]] = num_count[1]*[1]
        # nums[num_count[0]+num_count[1]:num_count[0]+num_count[1]+num_count[2]] = num_count[2]*[2]
        
