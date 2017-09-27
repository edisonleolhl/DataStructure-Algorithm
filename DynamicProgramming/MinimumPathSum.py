'''
Leetcode:
64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m > 0 and len(grid[0]) > 0:
            n = len(grid[0])
        else:
            return 0

        dp = [[0 for i in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            dp[i][0] = float('inf')
        for i in range(n+1):
            dp[0][i] = float('inf')
        dp[1][1] = grid[0][0]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    dp[i][j] = grid[i-1][j-1]
                elif dp[i-1][j] < dp[i][j-1]:
                    dp[i][j] = dp[i-1][j] + grid[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1] + grid[i-1][j-1]
        return dp[m][n]

grid = [
    [1]
]
print(Solution.minPathSum(Solution, grid))