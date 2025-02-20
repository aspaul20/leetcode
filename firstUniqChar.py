class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for char in s:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
        
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1 
        # for curr in range(len(s)):
        #     for i in range(len(s)):
        #         if i != curr and s[curr] == s[i]:
        #             break
        #     else:
        #         return curr
        
        # return -1
                
