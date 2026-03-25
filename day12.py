from aocd import get_data

data = get_data(day=12,year=2025)

example_data = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""

def parse_shape(shape):
    num, fill = shape.split(':\n')
    num = int(num)
    fill = [(i=='#')*1 for i in fill.replace('\n','')]
    return num, fill

def parse_areas(areas):
    parsed_areas = []
    for area in areas.split('\n'):
        size, req = area.split(': ')
        l = int(size.split('x')[0])
        w = int(size.split('x')[1])
        req = [int(i) for i in req.split(' ')]
        parsed_areas.append((l,w,req))
    return parsed_areas

def parse_data(data):
    sp = data.split('\n\n')
    shapes = sp[:-1]
    parsed_shapes = [parse_shape(shape) for shape in shapes]
    areas = sp[-1]
    parsed_areas = parse_areas(areas)
    return parsed_shapes, parsed_areas

data_to_use = example_data
parsed_shapes, parsed_areas = parse_data(data_to_use)

def can_fit(parsed_area, parsed_shapes):
    total_area = parsed_area[0] * parsed_area[1]
    needed_area = 0
    for i, m in enumerate(parsed_area[2]):
        needed_area += m*sum(parsed_shapes[i][1])
    if needed_area <= total_area:
        return True
    else:
        return False

def part_one(data):
    parsed_shapes, parsed_areas = parse_data(data)
    answer = 0
    for a in parsed_areas:
        answer += can_fit(a, parsed_shapes)
    return answer

part_one_answer = part_one(data)
