def Fibonacci(N):
    if N <= 1:
        return N
    else:
        return Fibonacci(N - 1) + Fibonacci(N - 2)

def main():
    while True:
        try:
            N = int(input("Enter an integer (-1 to exit): "))
            if N == -1:
                print("Program terminated!")
                break
            result = Fibonacci(N)
            print(f"Fibonacci({N}) = {result}")
        except:
            print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()
