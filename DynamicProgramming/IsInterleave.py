'''
Leetcode: 97 Interleaving String
题目描述：
输入三个字符串s1、s2和s3，判断第三个字符串s3是否由前两个字符串s1和s2交错而成，即不改变s1和s2中各个字符原有的相对顺序，
例如当s1 = “aabcc”，s2 = “dbbca”，s3 = “aadbbcbcac”时，则输出true，但如果s3=“accabdbbca”，则输出false。

思路：
多个字符串做“比较”的问题，大多都可以用DP求解。
构建二维数组，令dp[i][j]代表s3[0...i+j-1]是否由s1[0...i-1]和s2[0...j-1]的字符组成。
自然，我们的想法是遍历s3中的每个元素，然而要如何找到递推关系呢？
因为只需要输出true或false，那么我们可以只计算true的情形，其余情况全是false。
假设dp[i-1][j]为true，那么dp[i][j]为true的条件就是s1[i-1]是否等于s3[i+j-1]。
假设dp[i][j-1]为true，那么dp[i][j]为true的条件就是s2[j-1]是否等于s3[i+j-1]。
由此递推关系就可以求出。
'''

def isInterleave(s1, s2, s3):
    m = len(s1)
    n = len(s2)
    k = len(s3)
    if k != m + n:
        return False
    dp = [[False for i in range(n + 1)] for i in range(m + 1)]
    dp[0][0] = True
    # if s1[0] == s3[0]:
    #     dp[1][0] = True
    # if s2[0] == s3[0]:
    #     dp[0][1] = True
    for i in range(m+1):
        for j in range(n+1):
            if i != 0 or j != 0:
                if dp[i-1][j] is True and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = True
                elif dp[i][j-1] is True and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
    return dp[i][j]

s1 = "xyz"
s2 = "abc"
s3 = "xyzabc"
print(isInterleave(s1, s2, s3))