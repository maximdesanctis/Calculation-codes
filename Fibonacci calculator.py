def fibonacci(n):
    a = 0
    b = 1
    print(b)
    for i in range(n-1):
        a, b = b, a+b
        print(b)
    return b


n = int(input("Enter the number of the position of the fibonacci number you want to calculate..")) 
if "name" == "__main__":
    print("The number is " + str(fibonacci(n)) + " when you start with 1.")
