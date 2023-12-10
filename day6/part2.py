import util.file_handling
import re

def resolve():
    file_content = util.file_handling.read_file(".\\day6\\input.txt")
    parsed_input = parse_input(file_content)

    total = 1

    for k, game in parsed_input.items():
        print(game)
        lower_limit = find_lower_limit(game)
        print(lower_limit)
        upper_limit = find_upper_limit(game)
        print(upper_limit)
        total *= (upper_limit - lower_limit + 1)

    print(total)


    # test = (nummer - x)





def parse_input(file_content):

    test_input = {
        1: {
            "time": 71530,
            "distance": 940200
        }
    }

    real_input = {
        1: {
            "time": 52947594,
            "distance": 426137412791216
        }
    }

    return real_input


def find_lower_limit(game_input):

    seconds_standstill = 0

    while(True):

        driving_seconds = game_input["time"] - seconds_standstill
        speed = seconds_standstill
        distance = driving_seconds * speed

        if distance > game_input["distance"]:
            return seconds_standstill

        seconds_standstill += 1


def find_upper_limit(game_input):

    seconds_standstill = game_input["time"]

    while(True):
        seconds_standstill -= 1

        driving_seconds = game_input["time"] - seconds_standstill
        speed = seconds_standstill
        distance = driving_seconds * speed

        if distance > game_input["distance"]:
            return seconds_standstill
