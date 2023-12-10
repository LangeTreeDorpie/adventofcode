import util.file_handling
import re

def resolve():
    file_content = util.file_handling.read_file(".\\day7\\input.txt")
    parsed_input = parse_input(file_content)



def parse_input(file_content):
    regex = r"(\S+)\s(\d+)"
    matches = re.finditer(regex, file_content, re.MULTILINE)
