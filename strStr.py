class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0 
        end = start + len(needle)
        n = len(haystack)

        while end <= n: 
            end = start + len(needle)

            check = haystack[start:end]
            if check == needle:
                return start 
            
            start += 1
        return -1 
