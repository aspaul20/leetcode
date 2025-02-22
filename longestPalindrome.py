class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''

        for curr in range(len(s)):
            left = curr
            right = curr
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            substr = s[left+1:right]
            longest = substr if len(substr) >= len(longest) else longest

            left = curr
            right = curr+1
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            substr = s[left+1:right]
            longest = substr if len(substr) >= len(longest) else longest
            

        return longest 
