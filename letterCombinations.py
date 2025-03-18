class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
        }
        chars = list(digits)
        result = []

        def backtrack(i, current):
            if i >= len(digits):
                if current:
                    result.append(current)
                return 

            possible = mapping[chars[i]]
            for curr in possible:
                backtrack(i+1, current+curr)
            
        backtrack(0, '')
        return result
