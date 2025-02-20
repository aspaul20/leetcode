class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x!=0 and x%10 == 0):
            return False 
        
        reversd = 0
        while x > reversd:
            reversd = reversd*10 + x%10
            x = x//10
        return x == reversd or x == reversd//10
        # x_str = str(x)
        # start = 0 
        # end = len(x_str)-1

        # while start < end:
        #     if x_str[start]!=x_str[end]:
        #         return False
        #     start += 1
        #     end -= 1
        # return True 

        # x_str = str(x)
        # return True if x_str == x_str[::-1] else False
