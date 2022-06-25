class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = set()
        value = 0
        R = len(grid)
        C = len(grid[0])
        for ri, row in enumerate(grid):
            for ci, c in enumerate(grid[ri]):
                stack = [(ri, ci)]
                shape=0
                while stack:
                    r, c = stack.pop()
                    if grid[r][c] and not ((r,c) in seen):
                        seen.add((r,c))
                        shape+=1
                        if r+1<R:
                            stack.append((r+1,c))
                        if r-1>=0:
                            stack.append((r-1,c))
                        if c+1<C:
                            stack.append((r,c+1))
                        if c-1>=0:
                            stack.append((r,c-1))
                value = max(value, shape)
        return value

#Time Complexity O(n)