'''
Leetcode:
63. Unique Paths II

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n+1)] for i in range(m+1)]
        dp[1][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1] == 1:
                    dp[i][j] = 0
                elif i == 1 and j == 1:
                    dp[1][1] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m][n]

sol = Solution
obstacleGrid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(sol.uniquePathsWithObstacles(sol, obstacleGrid))