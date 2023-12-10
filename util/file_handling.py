

def read_file(file_name):

    with open(file_name) as f:
        return f.read()


def amount_of_lines_in_file(file_name):

    with open(file_name) as f:
        return len(f.readlines())
