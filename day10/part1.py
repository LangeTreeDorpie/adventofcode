import util.file_handling


def resolve():
    file_content = util.file_handling.read_file(".\\day10\\input.txt")
    grid, s_location, starting_locations = parse_input(file_content)

    pointer_one = starting_locations[0]
    previous_pointer_one = s_location

    pointer_two = starting_locations[1]
    previous_pointer_two = s_location

    count = 1

    while pointer_one != pointer_two:
        temp_one = pointer_one
        pointer_one = get_next_pos(grid, pointer_one, previous_pointer_one)
        previous_pointer_one = temp_one

        temp_two = pointer_two
        pointer_two = get_next_pos(grid, pointer_two, previous_pointer_two)
        previous_pointer_two = temp_two

        count += 1

    print("Answer:", count)


def parse_input(file_content):
    grid = list()
    s_location = None

    input_lines = str(file_content).split("\n")

    for i in range(0, len(input_lines)):

        line = list()
        for j in range(0, len(input_lines[i])):
            if input_lines[i][j] == "S":
                s_location = (i, j)
            line.append(input_lines[i][j])

        grid.append(line)

    return grid, s_location, get_possible_next_positions(grid, s_location)


def get_next_pos(grid, current_pos, previous_pos):
    possible_next_positions = get_possible_next_positions(grid, current_pos)

    for possible_next_position in possible_next_positions:
        if previous_pos != possible_next_position:
            return possible_next_position


def get_possible_next_positions(grid, current_pos):
    possible_delta_map = {
        "7": ((0, -1), (1, 0)),
        "L": ((-1, 0), (0, 1)),
        "F": ((0, 1), (1, 0)),
        "J": ((-1, 0), (0, -1)),
        "|": ((-1, 0), (1, 0)),
        "-": ((0, -1), (0, 1)),
        "S": ((-1, 0), (1, 0), (0, 1), (0, -1)),
        ".": ()
    }

    cur_x, cur_y = current_pos[0], current_pos[1]
    max_x, max_y = len(grid), len(grid[0])
    grid_icon = grid[cur_x][cur_y]
    possible_next_positions = list()

    for coordinate_delta in possible_delta_map[grid_icon]:
        new_x = cur_x + coordinate_delta[0]
        new_y = cur_y + coordinate_delta[1]

        if new_x < 0 or new_y < 0:
            continue

        if new_x > max_x or new_y > max_y:
            continue

        possible_next_positions.append((new_x, new_y))

    if grid_icon == "S":
        starting_positions = list()
        for possible_next_position in possible_next_positions:
            if current_pos in get_possible_next_positions(grid, possible_next_position):
                starting_positions.append(possible_next_position)
        return starting_positions

    return possible_next_positions
