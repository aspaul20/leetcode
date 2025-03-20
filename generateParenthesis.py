class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(current, open_count, close_count):
            if open_count == close_count == n:
                result.append(current)
                return
            if open_count < n: 
                current = current + '('
                backtrack(current, open_count+1, close_count)
                current = current[:-1]
            if close_count < open_count:
                current = current + ')'
                backtrack(current, open_count, close_count+1)
                current = current[:-1]

        backtrack('', 0, 0)
        return result 

