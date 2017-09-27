'''
Leetcode:
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        c = [[0 for i in range(n+1)] for i in range(m+1)]
        for i in range(n+1):
            c[0][i] = 0
        for i in range(m+1):
            c[i][0] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    c[i][j] = 1
                else:
                    c[i][j] = c[i-1][j] + c[i][j-1]
        return c[i][j]

sol = Solution()
print(sol.uniquePaths(1, 1))