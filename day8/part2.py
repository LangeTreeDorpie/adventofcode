import util.file_handling
import re
import math


def resolve():
    file_content = util.file_handling.read_file(".\\day8\\input.txt")
    instructions, directions, starting_points = parse_input(file_content)

    step_count = 0
    current_pointers = list(starting_points.keys())
    instruction_count = len(instructions)
    cases_found = 0

    while cases_found != len(starting_points.items()):
        next_instruction = instructions[step_count % instruction_count]

        for index in range(0, len(current_pointers)):
            if current_pointers[index][2] == "Z":
                continue

            starting_points[list(starting_points.keys())[index]] += 1
            current_pointer = current_pointers[index]
            current_pointers[index] = directions[current_pointer][next_instruction]

            if current_pointers[index][2] == "Z":
                cases_found += 1

        step_count += 1

    print(starting_points)
    print("Least Common Multiple:", find_multiple_of_numbers(list(starting_points.values())))


def parse_input(file_content):

    raw_instruction_string, raw_direction_string = str(file_content).split("\n\n")

    instructions = [0 if char == 'L' else 1 for char in raw_instruction_string]
    starting_points = dict()
    directions = dict()

    regex = r"(\w{3})\s=\s\((\w{3}),\s(\w{3})\)"
    matches = re.finditer(regex, raw_direction_string, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        directions[match[1]] = (match[2], match[3])
        if match[1][2] == "A":
            starting_points[match[1]] = 0

    return instructions, directions, starting_points


def find_multiple_of_numbers(numbers):
    lcm_result = 1
    for number in numbers:
        lcm_result = lcm_result * number // math.gcd(lcm_result, number)
    return lcm_result
