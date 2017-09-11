def insertion_sort(L):
    N = len(L)
    if N <= 0:
        print("Please input correct list.")
        return
    for i in range(N): # i指示当前待排元素
        if L[i - 1] < L[i]: # 如果待排元素比已排序列的最后一个元素（最大的元素）还大，则直接加入已排序列
            continue
        temp = L[i]
        for j in range(i - 1, -1, -1): # i-1指示已排序列的最后一项，然后以此与当前待排元素比较，往前移动
            L[j + 1] = L[j]
            if L[j - 1] <= temp:
                L[j] = temp
                print(L)
                break
    return L


if __name__ == '__main__':
    L = [1, 8, 7, 6, 5, 4, 3, 2, 1]
    print("ordered sequence =",insertion_sort(L))