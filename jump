class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        left = right = 0 
        jumps = 0
        while right < n - 1:
            farthest = 0
            for i in range(left, right+1):
                farthest = max(farthest, i+nums[i])
            left = right+1
            right = farthest 
            jumps += 1
        return jumps 

        # memo = {}
        # n = len(nums)
        # def jump_from(i):
        #     if i >= n-1:
        #         return 0 
            
        #     if i in memo:
        #         return memo[i]

        #     min_jumps = float('inf')
            
        #     for curr_jump in range(1, nums[i]+1):
        #         if i + curr_jump < n:
        #             jumps_needed = jump_from(i+curr_jump)
        #             if jumps_needed < min_jumps:
        #                 min_jumps = jumps_needed+1
        #     memo[i] = min_jumps 
        #     return min_jumps 
        # return jump_from(0)
        # jumps = 0
        # def jump_next(i, n, jumps, min_jumps):
            
        #     if i >= n-1:
        #         return jumps

        #     if jumps > min_jumps:
        #         return jumps 

        #     max_jumps = nums[i]

        #     for jump_idx in range(1, max_jumps+1):
        #         if i+jump_idx < n:
        #             jumps_needed = jump_next(i+jump_idx, n, jumps+1,min_jumps)
        #             if jumps_needed < min_jumps:
        #                 min_jumps = jumps_needed
            
        #     return min_jumps
        # return jump_next(0, len(nums), 0, float('inf'))
            
