class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        stack = []

        n_rows = len(board)
        n_cols = len(board[0])

        # checking '0' in top and bottom rows 
        for c in range(n_cols):
            if board[0][c] == "O":
                stack.append((0,c))
                board[0][c] = 1
            print(f"{n_rows-1=},{c=}")
            if board[n_rows-1][c] == "O":
                stack.append((n_rows-1,c))
                board[n_rows-1][c]=1
                
        # checking '0' in 2'nd and n-1 columns 
        for r in range(1,n_rows-1):
            if board[r][0] == "O":
                stack.append((r,0))
                board[r][0] = 1
            if board[r][n_cols-1] == "O":
                stack.append((r,n_cols-1))
                board[r][n_cols-1] = 1

        while stack:
            i,j = stack.pop()
            for di,dj in directions:
                ndi,ndj = i + di, j+ dj
                if 0 < ndi < n_rows and 0< ndj < n_cols and board[ndi][ndj] == "O":
                    stack.append((ndi,ndj))
                    board[ndi][ndj] = 1

        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == 1:
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"
        

        
        



            