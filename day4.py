from aocd import get_data
import numpy as np
from scipy import ndimage as ni

data = get_data(day=4,year=2025)
example_data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

def parse_data(data):
    parsed_data = []
    for row in data.split('\n'):
        cur_row = []
        for x in row:
            if x == '@':
                cur_row.append(1)
            else:
                cur_row.append(0)
        parsed_data.append(cur_row)
    return np.array(parsed_data)

def part_one(data):
    parsed_data = parse_data(data)
    kernel = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    adj_rolls = ni.convolve(parsed_data, kernel, mode='constant', cval=0)
    accessible = ((adj_rolls < 4) * 1) & (parsed_data)
    answer = np.sum(accessible)
    return answer

def part_two(data):
    parsed_data = parse_data(data)
    kernel = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    done = False
    answer = 0
    while not done:
        adj_rolls = ni.convolve(parsed_data, kernel, mode='constant', cval=0)
        accessible = ((adj_rolls < 4) * 1) & (parsed_data)
        now_accessible = np.sum(accessible)
        answer += now_accessible
        if now_accessible == 0:
            done = True
        for row, col in np.argwhere(accessible):
            parsed_data[row, col] = 0
    return answer


part_one_example_answer = part_one(example_data)
part_one_answer = part_one(data)

part_two_example_answer = part_two(example_data)
part_two_answer = part_two(data)