#Sorting - Makking array in ACD or DWSC way
#Sorting meothds - Insert/ Bubble/ Merge/ Selection
#logic - Algorithm 

def insertSort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
            A[i+1] = key

def findRange(A):
    range = A[-1] - A[0]
    return range

def findMedian(A):
    if len(A) % 2 == 0:
        median = ( A[len(A)//2] + A[len(A)//2 -1] ) /2 
    else:
        median = A[len(A)//2] 
    return median

def main():

    A =[]

    for i in range(9):
        index = int(input("Enter numbers: "))
        A.append(index)

    doInsertSort = insertSort(A)
    getRange = findRange(A)
    getMedian = findMedian(A)

    print(f"Sorted List is: {A}")
    print(f"Range of list A is: {getRange}")
    print(f"Median of list A is: {getMedian}")
    
    
if __name__ == "__main__":
    main()