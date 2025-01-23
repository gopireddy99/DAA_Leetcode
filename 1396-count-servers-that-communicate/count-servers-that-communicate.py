class Solution:
    def countServers(self, grid):
        rows, cols = len(grid), len(grid[0])
        row_count = [0] * rows
        col_count = [0] * cols

        # Count servers in each row and column
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        # Count servers that can communicate
        server_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    server_count += 1

        return server_count

solution = Solution()

grid1 = [[1, 0], [0, 1]]
grid2 = [[1, 0], [1, 1]]
grid3 = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

print(solution.countServers(grid1)) 
print(solution.countServers(grid2))
print(solution.countServers(grid3)) 
