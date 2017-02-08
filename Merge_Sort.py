def mergeSort(a):
    
    if len(a) > 1:
        mid = len(a)//2
        lefthalf = a[:mid]
        righthalf = a[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)        
        
        i = 0
        j = 0
        k = 0
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                a[k] = lefthalf[i]
                i += 1
            else:
                a[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            a[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            a[k] = righthalf[j]
            j += 1
            k += 1            
            
arr = [54,26,93,17,77,31,44,55,20]    
mergeSort(arr)
print arr