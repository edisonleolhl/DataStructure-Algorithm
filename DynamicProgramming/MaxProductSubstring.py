'''
题目描述：
给一个浮点数序列，取最大乘积连续子串的值，例如 -2.5，4，0，3，0.5，8，-1，则取出的最大乘积连续子串为3，0.5，8。
也就是说，上述数组中，3 0.5 8这3个数的乘积30.58=12是最大的，而且是连续的。

思路：
因为有正有负，所以每次都要存储最小的子串乘积值，因为下次要处理的 a[i] 可能是负，负负得正。

递推方程：
  maxend = max(max(maxend * a[i], minend * a[i]), a[i]);
  minend = min(min(maxend * a[i], minend * a[i]), a[i]);  
'''

def maxProductSubstring(a):
    maxend, minend, maxresult = a[0], a[0], a[0]
    for i in range(1,len(A)):
        maxend = max(max(maxend * a[i], minend * a[i]), a[i])
        minend = min(min(maxend * a[i], minend * a[i]), a[i])
        maxresult = max(maxend, maxresult)
    return maxresult

A = [-2.5, 4, 0, 3, 0.5, 8, -1]
print(maxProductSubstring(A))