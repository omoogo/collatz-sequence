def collatz(number):
    remainder = number % 2
    result = 0

    if remainder == 0:
        result = number // 2
    elif remainder == 1:
        result = 3 * number + 1

    print(result)
    return result


try:
    seed = int(input('Enter number: '))
    print(seed)
    while seed != 1:
        seed = collatz(seed)
except ValueError:
    print('You must enter an integer')


