def bubbleSort(A):
    n = len(A)
    for k in range (0,n):
        for j in range (0,n-k-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]