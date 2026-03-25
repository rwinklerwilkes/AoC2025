from aocd import get_data

data = get_data(day=1,year=2025)
example_data = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']

def parse_data(data):
    if not isinstance(data,list):
        data = data.split('\n')
    prelim = [(i[0],int(i[1:])) for i in data]
    data = [(-1*j if i == 'L' else j) for (i,j) in prelim]
    return data

def rotate(cur_pos, value, dial_size=100):
    return (cur_pos + value)%dial_size

def rotate_part_two(cur_pos, rotations, dial_size=100):
    zeros = 0
    #L358 from 59 should be 1 with 3 times passing 0
    if rotations < 0:
        zeros = abs(rotations) // 100
        rotations += zeros * dial_size #negative, so adding 100s onto this
        if cur_pos != 0 and cur_pos + rotations < 0:
            zeros += 1
    #R358 from 50 should be 8 with 4 times passing 0
    elif rotations > 0:
        zeros = rotations // 100
        rotations %= 100
        if cur_pos != 0 and cur_pos + rotations > dial_size:
            zeros += 1
    new_pos = (cur_pos + rotations)%dial_size
    if new_pos == 0:
        zeros += 1
    return new_pos, zeros

def part_one(data):
    parsed_data = parse_data(data)
    cur_pos = 50
    zeros = 0
    for val in parsed_data:
        cur_pos = rotate(cur_pos, val)
        zeros += (cur_pos == 0)*1
    return zeros

def part_two(data):
    parsed_data = parse_data(data)
    cur_pos = 50
    zeros = 0
    for val in parsed_data:
        print(f'Current position: {cur_pos}, rotating {val}')
        cur_pos, num_zeros = rotate_part_two(cur_pos, val)
        print(f'New position after: {cur_pos}, hit zero {num_zeros} times\n')
        zeros += num_zeros
    return zeros

part_one_example_answer = part_one(example_data)
part_one_answer = part_one(data)

part_two_example_answer = part_two(example_data)
part_two_answer = part_two(data)