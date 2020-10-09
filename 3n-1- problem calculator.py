def problem(n=100):
    if n == 1:
        return int(n)
    elif n == 0:
        return n
    elif n % 2 == 0:
        print(int(n))
        return problem(n / 2)
    else:
        print(int(n))
        return problem(3 * n + 1)

    
if __name__ == "__main__":
    print(problem(int(input("Enter number.."))))
