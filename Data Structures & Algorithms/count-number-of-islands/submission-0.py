

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        island = 0
        queue = []
        row = len(grid[0])
        col = len(grid)

        for c in range(col):
            for r in range(row):
                if grid[c][r] == "1":
                    # print(f"{grid[c][r]=}")
                    queue.append((c,r))
                    while queue:
                        # print(f"{queue=}")
                        i,j = queue.pop(0)
                        grid[i][j] = "0"
                        if j <row-1 and grid[i][j+1] == "1": #checking right
                            queue.append((i,j+1))
                            grid[i][j+1] = "0"
                        if i < col-1 and grid[i+1][j] == "1" : # checking down
                            queue.append((i+1,j))
                            grid[i+1][j] = "0"     
                        if  j>0 and grid[i][j-1] == "1": #checking left
                            queue.append((i,j-1))
                            grid[i][j-1] = "0"
                        if i>0 and grid[i-1][j] == "1": # checking up
                            queue.append((i-1,j))  
                            grid[i-1][j] = "0"   
                    island +=1
                    # print(f"{c=},{r=}")
        return island
                

                
