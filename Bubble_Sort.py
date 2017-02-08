def bubbleSort(a):
    passnum = len(a)-1
    exchanges = True
    while passnum > 0 and exchanges:
        i = 0
        exchanges = False
        while i < passnum:
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                exchanges = True
            i += 1
        passnum -= 1
    return a

arr = [54,26,93,17,77,31,44,55,20]
print bubbleSort(arr)
            