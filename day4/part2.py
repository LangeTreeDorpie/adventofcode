import math

import util.file_handling
import re


def resolve():
    file_name = ".\\day4\\input.txt"
    file_content = util.file_handling.read_file(file_name)
    regex = r"Card\s+(\d+): ([0-9 ]+)\S([0-9 ]+)"
    matches = re.finditer(regex, file_content, re.MULTILINE)

    extra_instances = dict()

    for x in range(1, util.file_handling.amount_of_lines_in_file(file_name) + 1):
        extra_instances[x] = 0

    for matchNum, match in enumerate(matches, start=1):
        game_id = int(match.group(1))
        winning_numbers = convert_string_to_map(match.group(2))
        numbers = convert_string_to_map(match.group(3))

        winning_numbers_matched = count_matching_numbers(winning_numbers, numbers)

        for x in range(1, winning_numbers_matched + 1):

            extra_instances[game_id + x] += extra_instances[game_id] + 1

    amount_of_instances = 0

    for k, v in extra_instances.items():
        amount_of_instances += v + 1

    print(amount_of_instances)
    print(extra_instances)



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
