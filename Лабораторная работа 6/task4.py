import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    with open(filename, 'r') as file:
        for line in file.readlines(1):
            titles = [elt.strip() for elt in line.split(',')]
        list_ = []
        for j in range(2, sum([1 for _ in open(filename)]) + 1):
            for line_1 in file.readlines(j):
                list_.append(dict(zip(titles, [elt.strip() for elt in line_1.split(',')])))

    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
