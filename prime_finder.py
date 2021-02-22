from prime_number_checker import *


def get_number():
    while True:
        enter = input("Enter a number to that you would like to check for primes.. ")
        try:
            enter = int(enter)
            return enter
        except ValueError:
            print("This is not a valid input for an integer")


def get_bool():
    while True:
        enter = input("Do you want to see a status?[True/False]")
        try:
            enter = bool(enter)
            return enter
        except ValueError:
            print("This is not a valid input for an integer")


def make_list(bound, status):
    primes = []
    one = ceil(bound / 100)
    if status:
        for i in range(bound):
            if i % one == 0:
                print(str(int(i/one)) + ' % done.. ')
            if check_for_prime(i, round_number(i)):
                primes.append(i)
            else:
                continue
    elif not status:
        for i in range(bound):
            if check_for_prime(i, round_number(i)):
                primes.append(i)
            else:
                continue
    return primes


if __name__ == '__main__':
    print(make_list(get_number(), get_bool()))
