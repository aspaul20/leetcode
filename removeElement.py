class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end = len(nums)-1
        k = 0 
        curr = 0
        while curr <= end:
            if nums[curr] == val:
                nums[curr], nums[end] = nums[end], nums[curr]
                end -= 1
            else:
                curr += 1
        return curr 
        # left, right = 0, 1
        # k = 0
        # while right < len(nums):
        #     # print(nums[i])
        #     if nums[left] == val and nums[right] == val and right+1 < len(nums):
        #         nums[right], nums[right+1] = nums[right+1], nums[right]
        #     if nums[left] == val:
        #         nums[left],nums[right]=nums[right],nums[left]
        #         k+= 1
        #     left += 1
        #     right += 1
        
        # return k
        # count = 0 
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[count] = nums[i]
        #         count += 1
            
        # return count
        # orig_len = len(nums)
        # nums.remove(val)
        # return orig_len-len(nums) + 1
        # ptr = 0
        # for i in range(len(nums)):
            
        #     if nums[i] != val: 
        #         nums[ptr] = nums[i]
        #         ptr += 1

        # return ptr 
