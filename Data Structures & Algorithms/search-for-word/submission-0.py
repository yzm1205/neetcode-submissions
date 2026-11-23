class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        
        n_rows = len(board)
        n_cols = len(board[0])
        def dfs(row, col, word_idx):
            if word_idx == len(word):
                    return True # base condition
            # check if current element is in word
            # first check bound case
            if not (0<= row < n_rows and 0<=col< n_cols) or board[row][col] != word[word_idx]:
                return False
            board[row][col] = "#"
            dirs = [(-1,0),(0,-1),(1,0),(0,1)]
            for r,c in dirs:
                nr,nc = row+r, col+c
                if dfs(nr,nc,word_idx+1):
                    return True
            #backtracking: replace all the hash with their respective word if we could find the word
            board[row][col] = word[word_idx]            
            return False
        # iterating over board to find starting element
        for r in range(n_rows):
            for c in range(n_cols):
                if dfs(r,c,0):
                    return True
        return False
        

        

                        

                    

