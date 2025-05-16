#Declaring Function multipy
def multipy(M,N):
    if M ==1:
        return M
    else:
         return M * multipy(M-1,N)
    

#Declaring a function to check if the number is prime or not
def main():
    while True:
        try:
            M = int(input("Enter 1st integer (Enter -1 to exit): "))
            if (M == -1):
                print("Exiting the program.")
                break
        except:
            print("Invalid input. Please enter an integer.")
            continue

        try:
            N=int (input("Enter 2nd integer: "))

            if (N == -1):
                print("Exiting the program.")
                break
        except:
            print("Enter valid integer")
            continue
        
        #Calling the function
        result =  multipy(M,N)

        print(f"The result of {M} * {N} is: {result}")
        print("Program terminated!")
        
        #Calling the main function
if __name__ == "__main__":
    main()
