from aocd import get_data
import numpy as np

data = get_data(day=3,year=2025)
example_data = '''987654321111111
811111111111119
234234234234278
818181911112111'''

def parse_data(data):
    return data.split('\n')

def find_largest(bank):
    largest = None
    for i, val in enumerate(bank):
        for j in range(i+1, len(bank)):
            val_j = bank[j]
            comp_int = int(val + val_j)
            if largest is None or comp_int > largest:
                largest = comp_int
    return largest

def part_one(data):
    parsed_data = parse_data(data)
    answer = 0
    for bank in parsed_data:
        answer += find_largest(bank)
    return answer

part_one_example_answer = part_one(example_data)
part_one_answer = part_one(data)

def parse_data_part_two(data):
    return [[int(c) for c in i] for i in data.split('\n')]

def find_lgst(bank, num_to_find):
    number = ''
    already_found = 0
    max_index = -1
    while already_found < num_to_find:
        start_index = max_index + 1
        end_index = len(bank) - (num_to_find - already_found)
        max_index = start_index + np.argmax(bank[start_index:end_index+1])
        number += f'{bank[max_index]}'
        already_found += 1
    return int(number)

def part_two(data):
    parsed_data = parse_data_part_two(data)
    answer = 0
    for bank in parsed_data:
        answer += find_lgst(bank,12)
    return answer

part_two_example_answer = part_two(example_data)
part_two_answer = part_two(data)