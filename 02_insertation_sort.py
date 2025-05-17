def insertationSort(A):
    for k in range (1,len(A)):
        key = A[k]
        i = k -1 

        while i>=0 and A[i] > key:
            A[i+1] =  A[i]
            i = i-1
            A[i+1] = key

def main():
    A = []
    for i in range(10):
        marks = int(input("Enter marks: "))
        A.append(marks)

    marksList = insertationSort(A)
    highestMarks = A[-5:]
    minMarks = min(A)
    maxMarks = max(A)

    print(f"Marks: {marksList}")
    print(f"Highest Marks: {highestMarks}")
    print(f"Max marks: {maxMarks}")
    print(f"Min marks: {minMarks}")
    

if __name__ == "__main__":
    main()
