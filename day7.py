from aocd import get_data
from collections import defaultdict

data = get_data(day=7,year=2025)
example_data = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

def parse_data(data):
    splitters = set()
    start = None
    for rownum, row in enumerate(data.split('\n')):
        for colnum, col in enumerate(row):
            if col == '^':
                splitters.add((rownum,colnum))
            elif col == 'S':
                start = (rownum,colnum)
    return start, splitters

def run_beams(start, splitters):
    max_row = max([x[0] for x in splitters])
    cur_beams = set()
    cur_beams.add(start)
    added = 0
    while cur_beams:
        next_beams = set()
        possible_splits = set()
        while cur_beams:
            cur_row, cur_col = cur_beams.pop()
            next_row = cur_row + 1
            if next_row > max_row:
                continue
            if (cur_row+1, cur_col) in splitters:
                left = (cur_row + 1, cur_col - 1)
                right = (cur_row + 1, cur_col + 1)
                next_beams.add(left)
                next_beams.add(right)
                possible_splits.add((cur_row, cur_col))
            else:
                next_beams.add((cur_row + 1, cur_col))
        cur_beams = next_beams
        added += len(possible_splits)
        # print(added)
    return added

def run_beams_dict(start, splitters):
    max_row = max([x[0] for x in splitters])+1
    #Don't need to track the row - starts at 0, start[1]
    cur_beams = {start[1]:1}
    splits = 0
    for i in range(max_row):
        next_beams = defaultdict(int)
        for cb,n in cur_beams.items():
            if (i,cb) in splitters:
                left = cb-1
                right = cb+1
                next_beams[left] += n
                next_beams[right] += n
                splits += 1
            else:
                next_beams[cb] += n
        cur_beams = next_beams
    return splits, cur_beams


def part_one(data):
    start, splitters = parse_data(data)
    answer = run_beams(start, splitters)
    return answer

def part_two(data):
    start, splitters = parse_data(data)
    splits, beams = run_beams_dict(start,splitters)
    answer = sum(n for i,n in beams.items())
    return answer


part_one_example_answer = part_one(example_data)
part_one_answer = part_one(data)

part_two_example_answer = part_two(example_data)
part_two_answer = part_two(data)