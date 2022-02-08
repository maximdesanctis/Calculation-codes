
def average(path):
    file = open(path, 'r')
    value_sum = 0
    value_number = 0
    for line in file:
        print(line, end='')
        if 'n' in line:
            continue
        value_sum += float(line)
        value_number += 1
    file.close()
    value_average = value_sum / value_number
    if int(value_average) == value_average:
        value_average = int(value_average)
    return value_average


def main():
    print('Average: ' + str(average(input('Please enter the path of the file with the values.. '))))


if __name__ == '__main__':
    main()
