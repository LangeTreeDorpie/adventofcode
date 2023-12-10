import util.file_handling
import re

def resolve():
    file_content = util.file_handling.read_file(".\\day6\\input.txt")
    parsed_input = parse_input(file_content)

    total = 1

    for k, game in parsed_input.items():
        print(game)
        lower_limit = find_lower_limit(game)
        upper_limit = find_upper_limit(game)
        total *= (upper_limit - lower_limit + 1)

    print(total)





def parse_input(file_content):

    test_input = {
        1: {
            "time": 7,
            "distance": 9
        },
        2: {
            "time": 15,
            "distance": 40
        },
        3: {
            "time": 30,
            "distance": 200
        }
    }

    real_input = {
        1: {
            "time": 52,
            "distance": 426
        },
        2: {
            "time": 94,
            "distance": 1374
        },
        3: {
            "time": 75,
            "distance": 1279
        },
        4: {
            "time": 94,
            "distance": 1216
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

    seconds_standstill = game_input["distance"]

    while(True):
        seconds_standstill -= 1

        driving_seconds = game_input["time"] - seconds_standstill
        speed = seconds_standstill
        distance = driving_seconds * speed

        if distance > game_input["distance"]:
            return seconds_standstill
