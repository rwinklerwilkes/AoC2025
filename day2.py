from aocd import get_data

data = get_data(day=2,year=2025)
example_data = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'

def parse_data(data):
    output = []
    for rng in data.split(','):
        output.append([int(i) for i in rng.split('-')])
    return output

def is_invalid(i):
    str_i = str(i)
    n = len(str_i)//2
    return str_i[:n] == str_i[n:]

def part_one(data):
    parsed_data = parse_data(data)
    invalid_sum = 0
    for low, high in parsed_data:
        for i in range(low,high+1):
            if is_invalid(i):
                invalid_sum += i
    return invalid_sum

part_one_example_answer = part_one(example_data)
part_one_answer = part_one(data)

import math

def is_invalid_part_two(i):
    str_i = str(i)
    divisors = list(divisor_generator(len(str_i)))[:-1]
    is_invalid = False
    for d in divisors:
        d = int(d)
        substrings = {str_i[d * i:d*(i+1)] for i in range(len(str_i)//d)}
        if len(substrings) == 1:
            is_invalid = True
    return is_invalid


def divisor_generator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def part_two(data):
    parsed_data = parse_data(data)
    invalid_sum = 0
    for low, high in parsed_data:
        for i in range(low,high+1):
            if is_invalid_part_two(i):
                invalid_sum += i
    return invalid_sum

part_two_example_answer = part_two(example_data)
part_two_answer = part_two(data)