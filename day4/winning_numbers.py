import os
from functools import reduce

from read_task import read_task

PATH = os.getcwd() + '/input.txt'


def count_winning_numbers(win_nums: set[int], actual_nums: set[int]) -> int:
    winning = actual_nums.intersection(win_nums)
    return reduce(lambda num, _: num * 2, range(1, len(winning) + 1)) if winning else 0


# first star
def main():
    input_ = read_task(PATH)
    res = []

    for line in input_:
        _, numbers = line.strip().split(': ')
        winning, actual = numbers.strip().split(' | ')

        winning_set = {int(i) for i in winning.split(' ') if i.isdigit()}
        actual_set = {int(i) for i in actual.split(' ') if i.isdigit()}

        res.append(count_winning_numbers(winning_set, actual_set))

    return sum(res)


print(main())
