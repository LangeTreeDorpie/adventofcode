import util.file_handling


def resolve():
    file_content = util.file_handling.read_file(".\\day9\\input.txt")
    lines = parse_input(file_content)

    total_sum = 0

    for line in lines:
        combined_list = list()
        combined_list.append(line)

        history = recursive_thing(combined_list, 0)
        extend_history(history)
        total_sum += history[0][-1]

    print(total_sum)


def parse_input(file_content):
    input_lines = str(file_content).split("\n")
    return [list(map(int, s.split())) for s in input_lines]


def recursive_thing(combined_list, recursion_depth):
    new_list = list()

    for index in range(0, len(combined_list[recursion_depth]) - 1):
        new_list.append(combined_list[recursion_depth][index + 1] - combined_list[recursion_depth][index])

    recursion_depth += 1
    combined_list.append(new_list)

    if all(x == 0 for x in new_list):
        return combined_list
    else:
        return recursive_thing(combined_list, recursion_depth)


def extend_history(history):

    for index in range(0, len(history) - 1):
        history[-2 - index].append((history[-1 - index][-1] + history[-2 - index][-1]))

