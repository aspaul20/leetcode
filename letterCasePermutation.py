class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        def backtrack(i, new_str):
            if i >= len(s):
                result.append(new_str)
                return 
            if s[i].isalpha():
                backtrack(i+1, new_str+s[i].lower())
                backtrack(i+1, new_str+s[i].upper())
            else:
                backtrack(i+1, new_str+s[i])
        backtrack(0, "")
        return result
