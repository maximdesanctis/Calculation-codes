#  Calculation of a square root

a = float(input("Enter the number from which you want the square root.."))
b = float(input("Enter the starting value for the iterations.."))
c = int(input("Enter the number of iterations you want to run.."))

if __name__ == "__main__":
    for i in range(c):
        b = (1/2)*(b+a/b)
        print(b)
    print("The square root is approximately " + str(b) + ".")
