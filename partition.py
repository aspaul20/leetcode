class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(start, partition):
            if start == len(s):
                result.append(partition.copy())
                return 

            for i in range(start, len(s)):
                substr = s[start:i+1]
                if substr == substr[::-1]:
                    partition.append(substr)
                    backtrack(i+1, partition)
                    partition.pop()

        backtrack(0, [])
        return result
                
            
