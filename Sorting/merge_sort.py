def merge(left, right):
    lp, rp = 0, 0
    result = []
    while lp < len(left) and rp < len(right):
        if left[lp] <= right[rp]:
            result.append(left[lp])
            lp += 1
        else:
            result.append(right[rp])
            rp += 1
    result += left[lp:]
    result += right[rp:]
    return result

def merge_sort(alist):
    length = len(alist)
    if length == 1:
        return alist
    mid = length // 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])
    print("left = %s, right = %s"%(left,right))
    result = merge(left, right)
    print("merge:",result)
    return result

if __name__ == '__main__':
    alist = [1, 8, 7, 6, 5, 4, 3, 2, 1]
    print("ordered sequence =",merge_sort(alist))
