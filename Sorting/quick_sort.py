def quick_sort(L,low,high):
    if(low < high):
        pivotloc = partition(L,low,high)
        quick_sort(L,low,pivotloc-1)
        quick_sort(L,pivotloc+1,high)
    return L


def partition(L,low,high):
    if(low >= high):
        return
    pivotkey = L[low]
    while(low < high):
        while(low < high and L[high] >= pivotkey):
            high = high - 1
        L[low],L[high] = L[high],L[low]
        while(low < high and L[low] <= pivotkey):
            low = low + 1
        L[high],L[low] = L[low],L[high]
        print("pivotkey =",pivotkey)
        print(L,"\n")
    return low
    
if __name__ == '__main__':
    L = [1,8,7,6,5,4,3,2,1]
    print(quick_sort(L, 0, len(L)-1))
