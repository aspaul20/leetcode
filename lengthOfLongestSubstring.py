class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_len = 0 
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right-left+1)
        return max_len 

            # print(s[start], s[end], seen, max_len)


                # seen = {a, b, c}
                # s[end] = a 
                # move start up  

        # while start <= n: 
        #     end = start + 1
        #     while end < n and s[end] != s[end-1] and s[end] != s[start]:
        #         end += 1
        #     print(s[start:end], max_len)
        #     max_len = max(max_len, end-start)
        #     start = end
        # return max_len 
