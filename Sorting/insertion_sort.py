def insertion_sort(L):
    N = len(L)
    if N <= 0 :
        print("Please input correct list.")
        return
    for i in range(N):
        temp = L[i]
        for j in range(i-1,-1,-1):
            L[j+1] = L[j]
            if j == 0 or L[j-1] < temp < L[j+1]:
                L[j] = temp
                print(L)
    return L

if __name__ == '__main__':
    L = [9,8,7,6,5,4,3,2,1]
    print(insertion_sort(L))
