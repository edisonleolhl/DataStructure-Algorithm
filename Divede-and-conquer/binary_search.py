def binary_search(A, x, low, high):
    if low == high:
        return -1
    mid = (low + high) // 2
    if A[mid] == x:
        return mid
    result_left = binary_search(A, x, low, mid)
    print("left", result_left)
    result_right = binary_search(A, x, mid+1, high)
    print("right", result_right)
    if result_left != -1:
        return result_left
    elif result_right != -1:
        return result_right
    else:
        return -1

A = list(range(10))
print(binary_search(A, 3, 0, len(A)-1))