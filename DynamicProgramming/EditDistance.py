'''
Leetcode:72. Edit Distance
题目描述：
给定一个源串和目标串，能够对源串进行如下操作：
1. 在给定位置上插入一个字符
2. 替换任意字符
3. 删除任意字符
写一个程序，返回最小操作数，使得对源串进行这些操作后等于目标串，源串和目标串的长度都小于2000。

思路：
动态规划，构建二维数组，注意二维数组的第0行和第0列不是全0的。
可以想象，如果source 为空，想要转换为 target，则肯定要执行 len(target) = n 次操作，所以dp[i][j]赋初值时要注意这点。

递推方程：
//dp[i,j]表示表示源串S[0…i] 和目标串T[0…j] 的最短编辑距离
dp[i, j] = min { dp[i - 1, j] + 1,  dp[i, j - 1] + 1,  dp[i - 1, j - 1] + (s[i] == t[j] ? 0 : 1) }
//分别表示：删除1个，添加1个，替换1个（相同就不用替换）。

解释：
插入是A在和B的前j-1个比，然后再在A的基础上进行插入一个字符，插入的字符是B的第j位，所以插入的代价是dp[i][j-1]+c0
删除是A的前i-1个和B的j个比，因为把A删除了一个字符，所以删除的代价是dp[i-1][j]+c1
替换是A的前i-1个和B的j-1个比，然后把A的第i位变成B的第j位。所以编辑的代价是dp[i-1][j-1]+c2
'''

def editDistance(source, target):
    m = len(source)
    n = len(target)

    dp = [[0 for i in range(n+1)] for i in range(m+1)]
    for i in range(n+1):
        dp[0][i] = i
    for i in range(m+1):
        dp[i][0] = i

    for i in range(1, m+1):
        for j in range(1, n+1):
            if source[i-1] == target[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(min(dp[i][j-1], dp[i-1][j]), dp[i-1][j-1]) + 1
    return dp[m][n]

source = "abc"
target = "axxxbxxxc"
print(editDistance(source, target))