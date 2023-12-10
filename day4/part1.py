import math

import util.file_handling
import re


def resolve():
    file_content = util.file_handling.read_file(".\\day4\\input.txt")
    regex = r"Card\s+(\d+): ([0-9 ]+)\S([0-9 ]+)"

    matches = re.finditer(regex, file_content, re.MULTILINE)
    total_points = 0;

    for matchNum, match in enumerate(matches, start=1):
        game_id = int(match.group(1))
        winning_numbers = convert_string_to_map(match.group(2))
        numbers = convert_string_to_map(match.group(3))

        winning_numbers_matched = count_matching_numbers(winning_numbers, numbers)

        game_points = int(math.pow(2, winning_numbers_matched-1))

        total_points += game_points

        print("Game id {} has {} points".format(game_id, game_points))

    print("total_points {}".format(total_points))


def convert_string_to_map(input):
    numbers = list()
    regex = r"(\d{1,2})"
    matches = re.finditer(regex, input, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        numbers.append(int(match.group(1)))

    return numbers


def count_matching_numbers(list_a, list_b):
    amount_of_matches = 0

    for item in list_a:
        try:
            list_b.index(item)
            amount_of_matches += 1
        except:
            pass

    return amount_of_matches
