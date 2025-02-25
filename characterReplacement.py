from collections import Counter 

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_count = 0
        longest = 0
        curr_count = Counter()
        for right in range(len(s)):
            char = s[right]
            curr_count[char] += 1
            max_count = max(curr_count[char], max_count) 
            if right-left+1 - max_count > k:
                curr_count[s[left]] -= 1
                left+= 1
            longest = max(longest, right-left+1)
        return longest


        # start = 0
        # max_count = 0
        # max_length = 0
        # count = [0] * 26  # For counting occurrences of characters A-Z

        # for end in range(len(s)):
        #     count[ord(s[end]) - ord('A')] += 1
        #     max_count = max(max_count, count[ord(s[end]) - ord('A')])
            
        #     while (end - start + 1) - max_count > k:
        #         count[ord(s[start]) - ord('A')] -= 1
        #         start += 1
            
        #     max_length = max(max_length, end - start + 1)
        # return max_length
        
