# prime number checker

def get_number():
    while True:
        enter = input("Enter a number you would like to check for prime:")
        try:
            enter = int(enter)
            return enter
        except ValueError:
            print("This is not a valid input for a natural number")


def check_for_prime(num, bool_value):
    divisors = []
    for i in range(2, num):
        if num % i == 0:
            divisors.append(i)
        elif i == num - 1:
            if not divisors:
                return True
            else:
                if bool_value:
                    return divisors
                else:
                    return False
        else:
            continue


number = get_number()

if __name__ == "__main__":
    if check_for_prime(number, False):
        print("This number is prime! ")
    else:
        print("This number is not prime")
        print("It is divisible by: ", check_for_prime(number, True))
