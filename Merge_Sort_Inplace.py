def merge_sort(xs):
    """Inplace merge sort of array without recursive. The basic idea
    is to avoid the recursive call while using iterative solution. 
    The algorithm first merge chunk of length of 2, then merge chunks
    of length 4, then 8, 16, .... , until 2^k where 2^k is large than 
    the length of the array
    """
    
    unit = 1
    while unit <= len(xs):
        h = 0
        for h in range(0, len(xs), unit * 2):
            l, r = h, min(len(xs), h + 2 * unit)
            mid = h + unit
            # merge xs[h:h + 2 * unit]
            p, q = l, mid
            while p < mid and q < r:
                if xs[p] < xs[q]: p += 1
                else:
                    tmp = xs[q]
                    xs[p + 1: q + 1] = xs[p:q]
                    xs[p] = tmp
                    p, mid, q = p + 1, mid + 1, q + 1

        unit *= 2
    
    return xs

arr = [54,26,93,17,77,31,44,55,20]    
print merge_sort(arr)
