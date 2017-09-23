'''
input: an array
output: the max 2 numbers in the array
'''

from timeit import Timer

def max2_force(A):
    x1 = -float('inf')
    x2 = -float('inf')
    for i in range(len(A)):
        if A[i] > x1:
            x1 = A[i]
            j = i
    for i in range(j):
        if A[i] > x2:
            x2 = A[i]
    for i in range(j + 1, len(A)):
        if A[i] > x2:
            x2 = A[i]
    return x1, x2


def max2_force_improve(A):
    x1 = -float('inf')
    x2 = -float('inf')
    for i in range(len(A)):
        if A[i] > x2:
            x2 = A[i]
            if x2 > x1:
                x1, x2 = x2, x1
    return x1, x2

def max2_divide_and_conquer(A, low, high):
    if low == high:
        return A[low], A[low]
    elif low + 1 == high:
        if A[low] > A[high]:
            return A[low], A[high]
        else:
            return A[high], A[low]
    else:
        mid = (low + high) // 2
        x1_left, x2_left = max2_divide_and_conquer(A, low, mid)
        x1_right, x2_right = max2_divide_and_conquer(A, mid + 1, high)
        if x1_left > x1_right:
            if x2_left > x1_right:
                return x1_left, x2_left
            else:
                return x1_left, x1_right
        else:
            if x2_right > x1_left:
                return x1_right, x2_right
            else:
                return x1_right, x1_left

A = [5,9,9,1]
print("max2_force: x1 = %s, x2 = %s"
      %(max2_force(A)[0], max2_force(A)[1]))

print("max2_force_improve: x1 = %s, x2 = %s"
      %(max2_force_improve(A)[0], max2_force_improve(A)[1]))

print("max2_divide_and_conquer: x1 = %s, x2 = %s"
      %(max2_divide_and_conquer(A, 0, len(A)-1)[0], max2_divide_and_conquer(A, 0, len(A)-1)[1]))

print("---------test speed--------")

t1 = Timer("max2_force([9,2,3,5,12,4,7,1,0])", "from __main__ import max2_force")
print("max2_force(A) ", t1.timeit(number=1000), "seconds")

t1 = Timer("max2_force_improve([9,2,3,5,12,4,7,1,0])", "from __main__ import max2_force_improve")
print("max2_force_improve(A) ", t1.timeit(number=1000), "seconds")

t1 = Timer("max2_divide_and_conquer([9,2,3,5,12,4,7,1,0], 0, len([9,2,3,5,12,4,7,1,0])-1)",
           "from __main__ import max2_divide_and_conquer")
print("max2_divide_and_conquer(A, low, high) ", t1.timeit(number=1000), "seconds")
