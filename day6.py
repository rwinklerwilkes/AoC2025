from aocd import get_data
import numpy as np
import itertools

data = get_data(day=6,year=2025)
example_data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +"""

def parse_data(data):
    raw_values = [[val for val in row.split(' ') if val] for row in data.split('\n')]
    unconverted_values = np.array(raw_values).T
    m = unconverted_values.shape[1]
    values = unconverted_values[:,0:m-1].astype(int)
    operators = unconverted_values[:,m-1]
    return values, operators

def part_one(data):
    answer = 0
    values, operators = parse_data(data)
    for i, op in enumerate(operators):
        cur_row = values[i,:]
        if op == '*':
            answer += np.multiply.reduce(cur_row)
        else:
            answer += np.add.reduce(cur_row)
    return answer

part_one_example_answer = part_one(example_data)
part_one_answer = part_one(data)

def parse_data_part_two(data_to_use):
    #Go through and find all column separators
    def is_all_spaces(column) -> bool:
        return all(char == " " for char in column)

    column_splits = []
    data_split = data_to_use.split('\n')
    ln = len(data_split[0])
    last = 0
    for i in range(ln):
        vals = [c[i] for c in data_split[:-1]]
        if is_all_spaces(vals):
            column_splits.append((last, i))
            last = i + 1
    column_splits.append([last, ln])

    #Then, split each row at each identified column separator, adding in 0s where there are spaces to help me
    #with number padding
    parsed_data = []
    operators = [i for i in data_split[-1].split(' ') if i]
    for row in data_split[:-1]:
        row_to_append = []
        for start, end in column_splits:
            row_to_append.append(row[start:end].replace(' ', '0')[::-1])
        parsed_data.append(row_to_append)

    #Transpose so that we're now reading left to right
    parsed_data = np.array(parsed_data).T
    new_parsed_data = []

    #Take the nth digit of each entry as the nth digit of each number, replacing 0 with empty string to remove
    #non-significant digits
    for row in parsed_data:
        new_row = []
        for i in itertools.zip_longest(*row):
            j = [x.replace('0', '') for x in i if x]
            new_row.append(int(''.join(j)))
        new_parsed_data.append(new_row)
    values = new_parsed_data
    return values, operators

def part_two(data):
    answer = 0
    values, operators = parse_data_part_two(data)
    for i, op in enumerate(operators):
        cur_row = values[i]
        if op == '*':
            answer += np.multiply.reduce(cur_row)
        else:
            answer += np.add.reduce(cur_row)
    return int(answer)

part_two_example_answer = part_two(example_data)
part_two_answer = part_two(data)