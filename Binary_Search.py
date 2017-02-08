def binarySearchRecursive(arr,low,mid,high,searchValue):
    """
    Recursive implementation for a Binary Search
    """
    print "\nRecursive Binary Search method called."
    if low > high:
        print "\nElement not found in the array."
        #index = -1
        return -1 
    if searchValue < arr[mid]:
        high = mid - 1
        mid = (low+high)/2
        return binarySearchRecursive(arr,low,mid,high,searchValue)
    elif searchValue > arr[mid]:
        low = mid + 1
        mid = (low+high)/2
        return binarySearchRecursive(arr,low,mid,high,searchValue)
    else:
        print "\nThe value %s being searched for was found at index : %d" % (searchValue,mid)
        return mid

def binarySearchIterative(arr,low,mid,high,searchValue):
    """
    Iterative implementation for a Binary Search
    """
    print "\nIterative Binary Search method called."
    while not low > high:
        if arr[mid] == searchValue:
            print "\nThe value %s being searched for was found at index : %d" % (searchValue,mid)
            return mid
        elif searchValue < arr[mid]:
            high = mid - 1
            mid = (low+high)/2
            continue
        elif searchValue > arr[mid]:
            low = mid + 1
            mid = (low+high)/2
            continue
    print "\nElement not found in the array."
    return -1

a = [1,2,3,4,5]                

for i in xrange(5):
    assert binarySearchRecursive(a,0,(len(a)+1)//2,len(a)-1,i+1) == i
    assert binarySearchIterative(a,0,(len(a)+1)//2,len(a)-1,i+1) == i