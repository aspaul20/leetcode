class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        
        def backtrack(i, total, current):
            if total == target:
                result.append(current.copy())
                return 

            if i >= len(candidates) or total > target:
                return 

            current.append(candidates[i])
            backtrack(i, total+candidates[i], current)
            current.pop()
            backtrack(i+1, total, current)
        
        backtrack(0, 0, [])
        return result
