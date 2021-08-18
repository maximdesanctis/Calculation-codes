# A program that solves a matrix
# At least 2x2 matrix
import tool_collection
import numpy as np


def get_lines():
    while True:
        try:
            matrix_lines = int(input('How many lines does the matrix have? '))
            return matrix_lines
        except ValueError:
            print('This is no valid input')


def get_columns():
    while True:
        try:
            matrix_columns = int(input('How many columns does the matrix have? '))
            return matrix_columns
        except ValueError:
            print('This is no valid input')


def get_matrix(matrix_lines, matrix_columns):
    matrix_matrix = []
    for line in range(matrix_lines):
        matrix_line = []
        for column in range(matrix_columns):
            value = tool_collection.get_input(f'Please enter the value ({line + 1}, {column + 1}) ', float)
            try:
                value = int(value)
            except ValueError:
                pass
            matrix_line.append(value)
        matrix_matrix.append(matrix_line)
    return matrix_matrix  # returns a list with all values


def eliminate(solve_matrix, matrix_lines, matrix_columns):
    for column in range(matrix_columns - 1):
        reference_line = solve_matrix[column]
        reference_value = solve_matrix[column][column]
        counter = 0
        i = -column
        while reference_value == 0:
            reference_value = solve_matrix[column][column]
            cache_one = solve_matrix[column]
            cache_two = solve_matrix[column + i]
            solve_matrix[column + i] = cache_one
            solve_matrix[column] = cache_two
            solve_matrix[column + i] = solve_matrix[column]
            i += 1
        for lin_position in range(matrix_lines):
            line = solve_matrix[lin_position]
            if line == solve_matrix[column]:
                counter += 1
                continue
            if counter == 0:
                continue
            reference_ratio = line[column] / reference_value
            for col_position in range(matrix_columns):
                line[col_position] -= reference_ratio * reference_line[col_position]
            solve_matrix[lin_position] = line
    return solve_matrix


def simplify(matrix_matrix, matrix_lines):
    reference = None
    for line_pos in range(matrix_lines):
        line = matrix_matrix[line_pos]
        counter = 0
        new_line = []
        for column in line:
            if column == 0:
                new_line.append(column)
                continue
            elif column != 0 and counter == 0:
                counter += 1
                reference = column
                column = 1
                new_line.append(column)
                continue
            else:
                column /= reference
                new_line.append(column)
        matrix_matrix[line_pos] = new_line
    return matrix_matrix


def clean(some_matrix):
    return_matrix = []
    for line in some_matrix:
        new_line = []
        for number in line:
            if int(number) == number:
                number = int(number)
            else:
                pass
            new_line.append(number)
        return_matrix.append(new_line)
    return return_matrix


def substitute(matrix_matrix, matrix_lines, matrix_columns):
    for col_pos in range(-2, -matrix_columns, -1):
        for line_pos in range(col_pos, -matrix_lines - 1, -1):
            matrix_matrix[line_pos][-1] -= matrix_matrix[line_pos][col_pos] * matrix_matrix[col_pos + 1][-1]
            matrix_matrix[line_pos][col_pos] = 0
    return matrix_matrix


def solution_check(matrix_matrix):
    for line in range(len(matrix_matrix)):
        for column in range(len(matrix_matrix[line]) - 1):
            if matrix_matrix[line][column] != 0 and line != column:
                return False
    return True


def rref(matrix, matrix_lines, matrix_columns):
    finished_matrix = clean(substitute(simplify(eliminate(matrix, matrix_lines, matrix_columns),
                                                matrix_lines), matrix_lines, matrix_columns))
    if solution_check(finished_matrix):
        return np.matrix(finished_matrix)
    else:
        print(finished_matrix)
        rref(finished_matrix, matrix_lines, matrix_columns)


if __name__ == '__main__':
    lines = get_lines()
    columns = get_columns()
    input_matrix = get_matrix(lines, columns)
    print('Input matrix: \n', np.matrix(input_matrix))

    solved_matrix = rref(input_matrix, lines, columns)
    print('Solved: \n', solved_matrix)
