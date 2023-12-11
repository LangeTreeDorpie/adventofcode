import time

import day4.part1
import day4.part2
import day5.part1
import day5.part2
import day6.part1
import day6.part2
import day7.part1
import day7.part2
import day8.part1
import day8.part2
import day9.part1
import day9.part2


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    start_time = time.time()

    # day4.part1.resolve()
    # day4.part2.resolve()
    # day5.part1.resolve()
    # day5.part2.resolve()
    # day6.part1.resolve()
    # day6.part2.resolve()
    # day7.part1.resolve()
    # day7.part2.resolve()
    # day8.part1.resolve()
    # day8.part2.resolve()
    # day9.part1.resolve()
    day9.part2.resolve()

    print("--- %s seconds ---" % (time.time() - start_time))
