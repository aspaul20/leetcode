class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        low, high = 0, len(s)-1
        while low <= high:
            while low < len(s)-1 and (s[low]==' ' or not s[low].isalnum()):
                low += 1

            while high >= 0 and (s[high]==' ' or not s[high].isalnum()):
                high -= 1

            if s[low] == s[high]:
                low+=1
                high-=1
            else:
                return False 
        return True 
