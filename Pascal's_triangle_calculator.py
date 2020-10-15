# A calculator for any row in Pascal's triangle
from math import factorial


def get_number():
    while True:
        user_input = input('Enter the line of Pascal\'s triangle you want to know..')
        try:
            user_input = int(user_input)
            if user_input > 0:
                return user_input
            else:
                print('The value must be greater than zero')
        except ValueError:
            print('This is not an integer')


def triangle_calculator(column):
    binomial_row = column - 1
    list_pascal = [1]
    for place in range(1, column):
        list_pascal.append(int((factorial(binomial_row)) / (factorial(place) * factorial(binomial_row - place))))
    return list_pascal


line = get_number()
line = triangle_calculator(line)
if __name__ == '__main__':
    print(line)
