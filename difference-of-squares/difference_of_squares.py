def square_of_sum(number):
    return factorial_one(number) ** 2


def sum_of_squares(number):
    return factorial_two(number)


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)


def factorial_one(number):
    if number == 1:
        return 1
    else:
        return number + factorial_one(number - 1)


def factorial_two(number):
    if number == 1:
        return 1
    else:
        return number ** 2 + factorial_two(number-1)
    