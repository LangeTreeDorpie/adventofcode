import util.file_handling


def resolve():
    file_content = util.file_handling.read_file(".\\day5\\input.txt")
    parsed_input = parse_input(file_content)

    print(parsed_input)

    mapped_seeds = merge_adjacent_ranges(parsed_input["seed_ranges"])

    for header, ranges in parsed_input.items():
        if header != "seed_ranges":
            mapped_seeds = map_ranges(mapped_seeds, ranges)

    print(mapped_seeds)

    print("Final answer is " + str(mapped_seeds[0][0]))


def parse_input(file_content):
    file_content_ranges = str(file_content).split("\n\n")

    parsed_input = dict()

    for file_content_range in file_content_ranges:
        if str(file_content_range).startswith("seeds: "):
            seeds_input = str(file_content_range)[7:]
            seeds_ranges = list(map(int, seeds_input.split(" ")))

            seeds_ranges_map = dict()

            for seed_range_index in range(0, int(len(seeds_ranges) / 2)):
                seed_range_start = seeds_ranges[seed_range_index * 2]
                seed_range_end = seed_range_start + seeds_ranges[(seed_range_index * 2) + 1]

                seeds_ranges_map[seed_range_start] = seed_range_end - 1

            parsed_input["seed_ranges"] = sorted(seeds_ranges_map.items(), key=lambda x: x[1])

            # print(sorted(seeds_ranges_map.items(), key=lambda x: x[1]))

        else:
            file_content_range = str(file_content_range).splitlines(keepends=False)
            file_content_header = file_content_range[0][:-5]
            parsed_input[file_content_header] = list()

            for i in range(1, len(file_content_range)):
                input_ranges = list(map(int, file_content_range[i].split(" ")))

                destination_range_start = input_ranges[0]
                source_range_start = input_ranges[1]
                range_length = input_ranges[2]

                start = source_range_start
                end = source_range_start + range_length - 1
                delta = destination_range_start - source_range_start

                parsed_input[file_content_header].append((start, end, delta))

    return parsed_input


def merge_adjacent_ranges(seed_ranges):
    seed_ranges = sorted(seed_ranges, key=lambda x: x[1])

    merged = []
    current_tuple = seed_ranges[0]

    for tpl in seed_ranges[1:]:
        if current_tuple[1] + 1 >= tpl[0]:
            current_tuple = (current_tuple[0], max(current_tuple[1], tpl[1]))
        else:
            merged.append(current_tuple)
            current_tuple = tpl

    merged.append(current_tuple)

    return merged


def map_ranges(mapped_seeds, input_range):
    overlapping_tuples = []

    for tuple1 in mapped_seeds:
        for tuple2 in input_range:
            overlap_start = max(tuple1[0], tuple2[0])
            overlap_end = min(tuple1[1], tuple2[1])

            if overlap_start < overlap_end:
                modifier = tuple2[2]
                overlapping_tuples.append((overlap_start + modifier, overlap_end + modifier))

    return merge_adjacent_ranges(overlapping_tuples)

