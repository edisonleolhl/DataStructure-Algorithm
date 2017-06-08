def shell_sort(L,delta):
    N = len(L)
    for inc in delta:
        L = shell_insert(L,inc)
        print(L,"\n")
    return L

def shell_insert(L,inc):
    N = len(L)
    for index in range(inc):               # 整个序列分为若干子序列，index是每个子序列的头元素
        for i in range(index+inc,N,inc):   # 默认每个子序列的头元素为“已排序列”，除了头元素的子序列为“待排序列”
            temp = L[i]                    # 每个子序列的排序方式为直接插入排序，所以当前待排元素的值给temp
            for j in range(i-inc,-1,-inc): # 在子序列的“已排序列”中找到合适的插入地点，所以是倒序
                if temp < L[j]:
                    L[j+inc] = L[j]
                else :
                    break                  # 当前待排元素比“已排序列”中的末尾元素还要大，所以直接放入末尾
                if j == index or L[j-inc] < temp :
                    L[j] = temp
                    print(L)
    return L

if __name__ == '__main__':
    L = [9,8,7,6,5,4,3,2,1]
    delta = [5,3,1] #构造增量序列
    print(shell_sort(L,delta))
