import util.file_handling


def resolve():
    file_content = util.file_handling.read_file(".\\day5\\input.txt")
    parsed_input = parse_input(file_content)
    print(parsed_input)

    mapped_seeds = dict()

    for seed in parsed_input["seeds"]:
        mapped_seeds[seed] = seed

    for header, ranges in parsed_input.items():
        if header != "seeds":
            print(header)
            print(map_source_to_target(mapped_seeds, ranges))
            print()

    lowest_value = 5000000000000000

    for original_seed_value, mapped_seed_value in mapped_seeds.items():
        if mapped_seed_value < lowest_value:
            lowest_value = mapped_seed_value

    print("Final answer is " + str(lowest_value))


def parse_input(file_content):
    file_content_ranges = str(file_content).split("\n\n")

    parsed_input = dict()

    for file_content_range in file_content_ranges:
        if str(file_content_range).startswith("seeds: "):
            seeds_input = str(file_content_range)[7:]
            parsed_input["seeds"] = list(map(int, seeds_input.split(" ")))
        else:
            file_content_range = str(file_content_range).splitlines(keepends=False)
            file_content_header = file_content_range[0][:-5]
            parsed_input[file_content_header] = list()

            for i in range(1, len(file_content_range)):
                parsed_input[file_content_header].append(list(map(int, file_content_range[i].split(" "))))

    return parsed_input


def map_source_to_target(mapped_seeds, input_range):
    for original_seed_value, mapped_seed_value in mapped_seeds.items():

        for input_ranges in input_range:
            destination_range_start = input_ranges[0]
            source_range_start = input_ranges[1]
            range_length = input_ranges[2]

            if source_range_start <= mapped_seed_value < source_range_start + range_length:
                mapped_seeds[original_seed_value] = mapped_seed_value + (destination_range_start - source_range_start)
                continue

    return mapped_seeds
