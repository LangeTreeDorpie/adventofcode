import util.file_handling
import re


def resolve():
    file_content = util.file_handling.read_file(".\\day8\\input.txt")
    instructions, directions = parse_input(file_content)

    step_count = 0
    current_pointer = "AAA"
    instruction_count = len(instructions)

    while current_pointer != "ZZZ":
        next_instruction = instructions[step_count % instruction_count]

        current_pointer = directions[current_pointer][next_instruction]
        step_count += 1

    print(step_count)


def parse_input(file_content):

    raw_instruction_string, raw_direction_string = str(file_content).split("\n\n")

    instructions = [0 if char == 'L' else 1 for char in raw_instruction_string]
    directions = dict()

    regex = r"(\w{3})\s=\s\((\w{3}),\s(\w{3})\)"
    matches = re.finditer(regex, raw_direction_string, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        directions[match[1]] = (match[2], match[3])

    return instructions, directions
