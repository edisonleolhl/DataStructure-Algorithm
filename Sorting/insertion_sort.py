def insertion_sort(L):
    N = len(L)
    if N <= 0:
        print("Please input correct list.")
        return
    for i in range(1, N): # i指示当前待排元素
        temp = L[i]
        for j in range(i-1, -1, -1): # i-1指示已排序列的最后一项，然后以此与当前待排元素比较，往前移动
            if L[j] <= temp:
                L[j+1] = temp
            else:
                L[j+1] = L[j]
                if j == 0:
                    L[j] = temp
    return L

def insertion_sort_desc(L):
    N = len(L)
    if N <= 0:
        print("Please input correct list.")
        return
    for i in range(1, N):
        temp = L[i]
        for j in range(i-1, -1, -1):
            if L[j] >= temp:
                L[j+1] = temp
            else:
                L[j+1] = L[j]
                if j == 0:
                    L[j] = temp
    return L

if __name__ == '__main__':
    L = [2, 8, 7, 6, 5, 4, 3, 2, 1]
    print("ordered sequence =", insertion_sort(L))
    print("ordered sequence descending = ", insertion_sort_desc(L))