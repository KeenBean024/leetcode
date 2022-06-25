class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        fresh, minutes = 0,0
        queue = deque()
        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    queue.append((i,j))
        directions = [[1,0], [-1,0], [0, 1], [0, -1]]
        while queue and fresh>0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row = r+dr
                    column = c+dc
                    if (0<=row<ROWS) and (0<=column<COLUMNS) and grid[row][column]==1:
                        queue.append((row, column))
                        grid[row][column]=2
                        if minutes==2:
                            print(minutes, row,column) 
                        fresh-=1
            minutes+=1
        return minutes if fresh==0 else -1
    
# TIME COMPLEXITY - O(n^2)
# SPACE COMPLEXITY - O(n^2)
