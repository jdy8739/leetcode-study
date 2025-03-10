# O(M*N*4^W) times, O(W) spaces
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
    
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col, idx):
            if idx == len(word):
                return True
            if not (0 <= row < rows and 0 <= col < cols):
                return False
            if board[row][col] != word[idx]:
                return False
            
            temp_val = board[row][col]
            board[row][col] = ""

            result = any(dfs(row+r, col+c, idx+1) for (r, c) in directions)

            board[row][col] = temp_val
            return result
    
        return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))
