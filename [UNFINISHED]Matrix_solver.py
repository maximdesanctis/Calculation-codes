# A program that solves a matrix


def get_number(user_input):
    while True:
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print('This is no valid input')


def solver(one, two, three, four):
    one = int(one[0])
    two = int(two[0])
    if three is not []:
        three = int(three[0])
    if four is not []:
        four = int(four[0])
    solved_sec = []
    solved_thr = []
    solved_fou = []
    for num1 in second_row:
        solved_sec.append(num1 - (num1/two) * one)
    try:
        for num2 in third_row:
            solved_thr.append(num2 - (num2/three) * two)
    except IndexError:
        print('No third line')
    try:
        for num3 in fourth_row:
            solved_fou.append(num3 - (num3/four) * three)
    except IndexError:
        print('No fourth line')
    return solved_sec, solved_thr, solved_fou


number_of_rows = get_number(input('Enter the number of rows the matrix has..'))
number_of_columns = get_number(input('Enter the number of columns the matrix has..'))

if __name__ == '__main__':
    first_row = []
    second_row = []
    third_row = []
    fourth_row = []
    for i in range(number_of_rows):
        if i + 1 == 1:
            print('First row')
            for n in range(number_of_columns):
                n = str(n + 1)
                first_row.append(get_number(input('Enter the number at position ' + n + ' .. ')))
            print(first_row)
        if i + 1 == 2:
            print('Second row')
            for n in range(number_of_columns):
                n = str(n + 1)
                second_row.append(get_number(input('Enter the number at position ' + n + ' .. ')))
            print(second_row)
        if i + 1 == 3:
            print('Third row')
            for n in range(number_of_columns):
                n = str(n + 1)
                third_row.append(get_number(input('Enter the number at position ' + n + ' .. ')))
            print(third_row)
        if i + 1 == 4:
            print('Fourth row')
            for n in range(number_of_columns):
                n = str(n + 1)
                fourth_row.append(get_number(input('Enter the number at position ' + n + ' .. ')))
            print(fourth_row)
    print(first_row, second_row, third_row, fourth_row)
    print(solver(first_row, second_row, third_row, fourth_row))
