def insertion_sort(L):
    N = len(L)
    if N <= 0 :
        print("Please input correct list.")
        return
    for index in range(2):
        for i in range(index,N,2):
            temp = L[i]
            for j in range(i-2,-1,-2):
                L[j+2] = L[j]
                if j == index or L[j-2] < temp < L[j+2]:
                    L[j] = temp
                    print(L)
    return L

if __name__ == '__main__':
    L = [9,8,7,6,5,4,3,2,1]
    print(insertion_sort(L))
