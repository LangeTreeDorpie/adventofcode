import util.file_handling
import re

def resolve():
    file_content = util.file_handling.read_file(".\\day7\\input.txt")
    parsed_input = parse_input(file_content)
    sorted_list = sorted(parsed_input, key=lambda x: int(x[0], 16))
    print(sorted_list)

    total = 0

    for x in range(0, len(sorted_list)):

        total += (sorted_list[x][1] * (x + 1))

    print(total)


def parse_input(file_content):
    regex = r"(\S+)\s(\d+)"
    matches = re.finditer(regex, file_content, re.MULTILINE)

    parsed_input = list()

    for matchNum, match in enumerate(matches, start=1):
        hex_string = map_to_hex_string(match[1])
        strength_value = parse_strength_value(match[1])

        hex_value = string_to_hex(strength_value + hex_string)
        bet_value = int(match[2])

        parsed_input.append((hex_value, bet_value))

    return parsed_input


def map_to_hex_string(input_string):

    non_number_map = {
        "T": "A",
        "J": "B",
        "Q": "C",
        "K": "D",
        "A": "E",
    }

    hex_string = ""

    for input_char in input_string:
        if is_string_a_number(input_char):
            hex_string += input_char
        else:
            hex_string += non_number_map[input_char]

    return hex_string


def string_to_hex(input_string):
    an_integer = int(input_string, 16)
    return hex(an_integer)


def parse_strength_value(input_string):

    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    duplicates = {char: count for char, count in char_count.items() if count > 1}
    strength_conditions = dict()

    for duplicate, times in duplicates.items():
        if times in strength_conditions:
            strength_conditions[times] += 1
        else:
            strength_conditions[times] = 1

    if 5 in strength_conditions:
        return "6"

    if 4 in strength_conditions:
        return "5"

    if 3 in strength_conditions:
        if 2 in strength_conditions:
            return "4"
        else:
            return "3"

    if 2 in strength_conditions:
        if strength_conditions[2] == 2:
            return "2"
        else:
            return "1"

    return "0"


def is_string_a_number(input_string):
    try:
        int(input_string)
        return True
    except Exception:
        return False
