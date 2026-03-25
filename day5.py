from aocd import get_data
data = get_data(day=5,year=2025)
example_data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

def parse_data(data):
    ranges,ingredients = data.split('\n\n')
    ranges = [[int(i) for i in row.split('-')] for row in ranges.split('\n')]
    ranges = sorted(ranges,key=lambda x:x[0])
    ingredients = [int(row) for row in ingredients.split('\n')]
    return ranges, ingredients

def is_fresh(ingredient, ranges):
    fresh = False
    for mn, mx in ranges:
        if ingredient >= mn and ingredient <= mx:
            fresh = True
            break
    return fresh

def part_one(data):
    ranges,ingredients = parse_data(data)
    answer = 0
    for i in ingredients:
        if is_fresh(i, ranges):
            answer += 1
    return answer

part_one_example_answer = part_one(example_data)
part_one_answer = part_one(data)

def overlaps(cur_mn, cur_mx, nxt_mn, nxt_mx):
    return max(cur_mn, nxt_mn) < min(cur_mx, nxt_mx)

def part_two(data):
    ranges, ingredients = parse_data(data)
    answer = 0
    current = -1
    for start, end in ranges:
        if current >= start:
            #Already counted this in an earlier range
            start = current + 1
        if start <= end:
            #Has some uncounted numbers here
            answer += end-start+1
        #Shift to the end of the current range and continue on
        current = max(current,end)
    return answer

part_two_example_answer = part_two(example_data)
part_two_answer = part_two(data)