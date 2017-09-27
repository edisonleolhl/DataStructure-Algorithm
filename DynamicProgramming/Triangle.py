'''
Leetcode:120. Triangle
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

'''


class Solution(object):
    '''
        extra space: O(n^2)
        using 'top to bottom' thought
    '''
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        length = len(triangle)
        dp = [[0 for i in range(j+1)] for j in range(length)] # dp[i][j] means element of row i column j is the last one of the min_path
        dp[0][0] = triangle[0][0]
        for i in range(1, length):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                elif dp[i-1][j] < dp[i-1][j-1]:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                else:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        return min(dp[length-1])

    '''
        extra space: O(n)
        using 'bottom to top' thought
    '''
    def minimumTotal_bottomtotop(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        length = len(triangle)
        dp = triangle[length-1]
        for i in range(length-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]

triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

# print(Solution.minimumTotal(Solution, triangle))
print(Solution.minimumTotal_bottomtotop(Solution, triangle))