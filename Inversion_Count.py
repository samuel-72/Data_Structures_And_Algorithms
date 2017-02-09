#Count Inversions
# Inversion - For 2 array indices i,j if arr[i] > arr[j] then it is an inversion
# Do Merge Sort, whenever you copy an element from the Right Half the number of inversion is equal to \n
# Left Half - Current Index at Left Half

def countInversion(A,inversion):
    # Merge Sort
    n = len(A)
    if n <= 1:
        return (A,0)
    else:
        p1, inv1 = countInversion(A[:n/2],inversion)
        p2, inv2 = countInversion(A[n/2:],inversion)
        i,j,k = 0,0,0
        inv = inv1 + inv2 
        while i < len(p1) and j < len(p2):
            if p1[i] <= p2[j]:
                A[k] = p1[i]
                i += 1
                k += 1
            else:
                A[k] = p2[j]
                j += 1
                k += 1
                inv += len(p1) - i
        while i < len(p1):
            A[k] = p1[i]
            i += 1
            k += 1
        while j < len(p2):
            A[k] = p2[j]
            j += 1
            k += 1
        return (A,inv)
    
def main():
    A1 = [9,4,7,5,8,1,2,3,6]
    print countInversion(A1,0)
    A2 = [54,26,93,17,77,31,44,55,20]
    print countInversion(A2,0)
    A3 = [1,3,5,2,4,6]
    print countInversion(A3,0)        
    
if __name__ == '__main__':
    main()