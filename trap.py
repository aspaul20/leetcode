class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        start = 0 
        end = n - 1

        max_left = height[start]
        max_right = height[end]

        while start < end:
            if max_left < max_right:
                start += 1 
                max_left = max(height[start], max_left)
                water += max(0, max_left-height[start])
            else:
                end -= 1
                max_right = max(height[end], max_right)
                water += max(0, max_right-height[end])

        return water 
        # water = 0
        # start = 0
        # n = len(height)

        # while start < n: 
        #     if height[start] == 0: 
        #         start += 1
        #         continue
            
        #     second_best = -1
        #     end = start+1

        #     while end < n:
        #         if height[end] >= height[start]:
        #             second_best = end 
        #             break 
        #         if second_best == -1 or height[end] > height[second_best]:
        #             second_best = end
        #         end += 1
            
        #     if second_best == -1:
        #         break 
            
        #     end = second_best
        #     traveled_width = end - start - 1

        #     if traveled_width <= 0:
        #         start = end 
        #         continue 
            
        #     smaller_height = min(height[start], height[end])
        #     total_area = traveled_width * smaller_height

        #     for i in range(start+1, end):
        #         total_area -= height[i]

        #     valley_sum = prefix[end] - prefix[start + 1]
        #     water += total_area - valley_sum
        #     start = end

        # return water



        # while start < n: 
        #     if height[start] == 0: 
        #         start+=1
        #         continue 
        #     else:
        #         end = start+1
        #         while end < n and height[end] <= height[start]:
        #             end += 1
        #         if end >= n:
        #             break
        #         print("water ", water)
        #         print(start, end)
        #         print(height[start], height[end])

        #         height_diff = abs(height[start]-height[end])
        #         traveled_width = end-start-1
                
        #         if height[start] > height[end]:
        #             smaller_height = height[end]
        #             iterator = end 
        #             total_area = smaller_height*traveled_width

        #             while iterator != start:
        #                 total_area -= height[iterator]
        #                 iterator -= 1
        #             print(f"Adding {total_area} b/w {height[start]}, {height[end]}, height: {smaller_height}, width: {traveled_width}")
        #             water += total_area

        #         elif height[end] > height[start]:
        #             smaller_height = height[start]
        #             iterator = start 
        #             total_area = smaller_height*traveled_width

        #             while iterator != end:
        #                 total_area -= height[iterator]
        #                 iterator += 1
                    
        #             print(f"Adding {total_area} b/w {height[start]}, {height[end]}, height: {smaller_height}, width: {traveled_width}")
        #             water += total_area
        #         start =end
                
        # return water
