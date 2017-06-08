def select_sort(L):
    N = len(L)
    if N <= 0 :
        print("Please input correct list.")
        return
    for i in range(N-1):
        indexOfMax = 0
        for j in range(1,N-i):
            if L[j] > L[indexOfMax] :
                indexOfMax = j
        L[N-1-i], L[indexOfMax] = L[indexOfMax], L[N-1-i]
        print(L)
    return L    

if __name__ == '__main__':
    L = [9,8,7,6,5,4,3,2,1]
    select_sort(L)
