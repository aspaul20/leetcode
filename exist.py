class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack(i, j, current, visited):

            nonlocal found 
            if current == word:
                found = True 
                return 
            
            if i < 0 or i >= rows or j < 0 or j >= cols or (i, j) in visited:
                return  

            to_find = word[len(current)]

            if board[i][j] == to_find:

                visited.add((i,j))

                backtrack(i+1, j, current+board[i][j], visited)
                backtrack(i-1, j, current+board[i][j], visited)
                backtrack(i, j+1, current+board[i][j], visited)
                backtrack(i, j-1, current+board[i][j], visited)

                visited.remove((i,j))

        found = False
        rows = len(board)
        cols = len(board[0])
        current = ''
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visited = set()
                    backtrack(i, j, current, visited)
                    if found:
                        return found 
        return found
