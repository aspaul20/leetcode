class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def dfs(i, total, curr):
            if total == target:
                return result.append(curr.copy())
            if total > target:
                return 

            for ite in range(i, len(candidates)):
                if ite > i and candidates[ite] == candidates[ite-1]:
                    continue
                curr.append(candidates[ite])
                dfs(ite+1, total+candidates[ite], curr)
                curr.pop()

        dfs(0, 0, [])
        return result
