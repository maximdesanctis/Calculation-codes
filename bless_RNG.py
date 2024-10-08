from random import randint
from time import time


def simulation_geese(n):
    kills = 0
    for i in range(n):
        number = str(randint(10000000000, 19999999999))[1:]
        number_of_killed_gooses = len(set(number))
        kills += number_of_killed_gooses

    average_kills = kills / n
    return average_kills


def simulation_maze(n):
    successes = 0
    for i in range(n):
        number = list(str(randint(10000000, 19999999))[1:])
        even = 0
        for digit in number:
            if int(digit) % 2 == 0:
                even += 1
        if even == 3:
            successes += 1
    success_rate = successes / n
    return success_rate


def simulation_birthday(n):
    collisions = 0
    for i in range(n):
        birthdays = []
        for person in range(20):  # 20 people
            birthdays.append(randint(1, 365))
        if len(set(birthdays)) < 20:
            collisions += 1
    return collisions / n


def main(option, times):
    path = input ("Please enter the path… ")
    starting_time = time()
    if option.lower() == 'goose':
        value = simulation_geese(times)
        file = open(f'{path}/values.txt', 'a')
        file.write('n = ' + str(times) + '\n')
        file.write(str(value) + '\n')
    if option.lower() == 'maze':
        value = simulation_maze(times)
        file = open(f'{path}/values_maze.txt', 'a')
        file.write('n = ' + str(times) + '\n')
        file.write(str(value) + '\n')
    if option.lower() == 'birthday':
        value = simulation_birthday(times)
        file = open(f'{path}/values_birthday.txt', 'a')
        file.write('n = ' + str(times) + '\n')
        file.write(str(value) + '\n')
    else:
        file = open('Text.txt')
    file.close()
    return time() - starting_time


if __name__ == '__main__':
    print(
        main(input('What do you want to simulate? '), int(input('How many times do you want to run the simulation? '))))
