def load_file(filename: str) -> list[str]:
    filename = 'inputs/' + filename
    input_list = []
    with open(filename, 'r') as inputfile:
        for line in inputfile:
            input_list.append(line)
    return input_list
