class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = float('-inf')
        start = 0 
        end = len(height) - 1

        while start <= end: 
            area = (end-start) * min(height[start], height[end])
            if area >= max_water:
                max_water = area 
            
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_water
        # low = 0 
        # high = len(height)-1
        # max_area = float('-inf')
        # while low < high:
        #     lower_pillar = height[low] if height[low] < height[high] else height[high]
        #     area = lower_pillar * (high-low)
        #     max_area = max(max_area, area)
        #     if height[low] < height[high]:
        #         low += 1
        #     else: 
        #         high -=1 
        # return max_area
        # max_area = 0
        # start = 0 
        # end = len(height)-1 

        # while start < end: 

        #     width = end-start 
        #     heigh = min(height[start], height[end])
        #     area = width * heigh  

        #     if area > max_area: 
        #         max_area = area 
        #     if height[start] > height[end]:
        #         end -=1 
        #     else: 
        #         start += 1 
        # return max_area
