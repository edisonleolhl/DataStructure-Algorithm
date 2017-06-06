def bubble_sort(L):
    N = len(L)
    if N <= 0 :
        print("Please input correct list.")
        return
    for i in range(N):
        for j in range(0,N-1-i):
            if L[j] > L[j+1] :
                L[j],L[j+1] = L[j+1],L[j]
                print(L)
    return L

if __name__ == '__main__':
    L = [9,8,7,6,5,4,3,2,1]
    print(bubble_sort(L))
