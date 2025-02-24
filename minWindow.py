from collections import Counter 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        min_window = ''
        min_len = float('+inf')

        gt_count = Counter(t)
        window_count = Counter()

        left = 0
        matched_count = 0 

        for right in range(len(s)):
            char = s[right]
            window_count[char] += 1 

            if char in gt_count and window_count[char] == gt_count[char]:
                matched_count += 1
            
            while matched_count == len(gt_count):
                if right-left+1 < min_len:
                    min_len = right-left+1
                    min_window = s[left:right+1]
                
                left_char = s[left]
                window_count[left_char] -= 1

                if left_char in gt_count and window_count[left_char] < gt_count[left_char]:
                    matched_count -= 1
                left += 1

        return min_window if min_len != float("inf") else ""
