from timeit import Timer


def di_cal_wrong(A):
    max_sub_sum = -float('inf')  # init
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if sum(A[i:j+1]) > max_sub_sum:
                max_sub_sum = sum(A[i:j+1])
                low = i
                high = j
    return(max_sub_sum, low, high)


def di_cal(A):
    sum = A[0]
    max_sub_sum = -float('inf')  # init
    for i in range(len(A)):
        sum = A[i]
        for j in range(i+1, len(A)):
            sum += A[j]
            if sum > max_sub_sum:
                max_sub_sum = sum
                low = i
                high = j
    return(max_sub_sum, low, high)


def find_cross_suming_subarray(A, mid, low, high):
    # 最大子数组横跨中点，所以最大子数组的左边是A[i..mid],右边是A[mid+1..j]
    # 求出某边的最大子数组可以直接用暴力求解法，暴力运行时间是 n ，分治操作是 logn ，所以这种方法能实现 O(nlogn)
    left_sum, right_sum = 0, 0
    max_left_sum, max_right_sum = -float('inf'), -float('inf')
    # 注意 range(start,stop,step)，包括start，不包括stop，所以对应的low-1与high+1
    for i in range(mid, low-1, -1):
        left_sum += A[i]
        if left_sum > max_left_sum:
            max_left_sum = left_sum
            low = i
    for j in range(mid+1, high+1, 1):
        right_sum += A[j]
        if right_sum > max_right_sum:
            max_right_sum = right_sum
            high = j
    return max_right_sum+max_left_sum, low, high


def divide_and_conquer(A, low, high):
    if low == high:
        return A[low], low, high
    mid = (low + high) // 2
    left_sum, left_low, left_high = divide_and_conquer(A, low, mid)
    print("left:", left_sum, left_low, left_high)
    right_sum, right_low, right_high = divide_and_conquer(A, mid+1, high)
    print("right:", right_sum, right_low, right_high)
    cross_sum, cross_low, cross_high = find_cross_suming_subarray(A, mid, low, high)
    print("cross:", cross_sum, cross_low, cross_high)
    if left_sum > right_sum and left_sum > cross_sum:
        return left_sum, left_low, left_high
    elif right_sum > left_sum and right_sum > cross_sum:
        return right_sum, right_low, right_high
    else:
        return cross_sum, cross_low, cross_high

def dp(A):
    low, high = 0, 0
    B = list(range(len(A)))
    B[0] = A[0]
    max_sub_sum = A[0]
    for i in range(1, len(A)):
        if B[i-1] > 0:
            B[i] = B[i-1] + A[i]
        else:
            B[i] = A[i]
            low = i
        if B[i] > max_sub_sum:
            max_sub_sum = B[i]
            high = i
    return max_sub_sum, low, high

def linear_time(A):
    sum, max_sub_sum, low, high, cur = 0, 0, 0, 0, 0
    for i in range(0, len(A)):
        sum += A[i]
        if sum > max_sub_sum:
            max_sub_sum = sum
            # 起点从0开始，从左往右操作
            low = cur
            high = i
        # 每当和小于0时，丢弃之前处理过的所有记录，最大和清0，并且起点从下一位开始
        if sum < 0:
            sum = 0
            cur = i + 1
    return max_sub_sum, low, high

A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]

# print(di_cal_wrong(A))
# print(di_cal(A))
#
# t1 = Timer("di_cal([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7])", "from __main__ import di_cal")
# print("di_cal ", t1.timeit(number=1000), "seconds")
#
# t1 = Timer("di_cal_wrong([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7])", "from __main__ import di_cal_wrong")
# print("di_cal_wrong ", t1.timeit(number=1000), "seconds")
#
# print(divide_and_conquer(A, 0, len(A)-1))
#
# print(linear_time(A))
print(dp(A))