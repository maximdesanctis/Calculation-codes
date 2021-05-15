# prime number checker
from math import ceil


def get_number():
    while True:
        enter = input("Enter a number you would like to check for prime:")
        try:
            enter = int(enter)
            return enter
        except ValueError:
            print("This is not a valid input for a natural number")


def prime_check(check_num):
    if check_num < 2:
        return False
    for pot_div in range(2, int(pow(check_num, 1 / 2))):
        if check_num % pot_div != 0:
            continue
        return False
    return True


if __name__ == "__main__":
    if prime_check(get_number):
        print("This number is prime! ")
    else:
        print("This number is not prime")
