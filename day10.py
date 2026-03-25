from aocd import get_data
from itertools import chain, combinations
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

data = get_data(day=10,year=2025)
example_data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

def parse_state(state_str):
    new_state = []
    for c in state_str:
        if c == '.':
            new_state.append(0)
        else:
            new_state.append(1)
    return new_state

def parse_data(data):
    parsed_data = []
    for row in data.split('\n'):
        sp = row.split(' ')
        expected = sp[0][1:-1]
        parsed_expected = parse_state(expected)
        button_size = len(expected)
        joltage = sp[-1][1:-1]
        joltage = [int(i) for i in joltage.split(',')]
        parsed_buttons = []
        buttons = sp[1:-1]
        for button in buttons:
            button_behavior = [0 for i in range(button_size)]
            remove_parens = button[1:-1]
            int_buttons = [int(i) for i in remove_parens.split(',')]
            for i in int_buttons:
                button_behavior[i] = 1
            parsed_buttons.append(button_behavior)
        parsed_data.append((parsed_expected, parsed_buttons, joltage))
    return parsed_data

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def press_all_buttons(expected, buttons):
    min_presses = np.inf
    for press_set in powerset(buttons):
        state = [0 for i in range(len(expected))]
        for button in press_set:
            state = np.logical_xor(state, button)
        if np.all(expected == state) and len(press_set) < min_presses:
            min_presses = len(press_set)
    return min_presses


def part_one(data):
    parsed_data = parse_data(data)
    answer = 0
    for expected, buttons, _ in parsed_data:
        min_presses = press_all_buttons(expected, buttons)
        answer += min_presses
    return answer

part_one_example_answer = part_one(example_data)
part_one_answer = part_one(data)

###############PART TWO FOLLOWS###############

def part_two(data):
    parsed_data = parse_data(data)
    answer = 0
    for _, buttons, joltage in parsed_data:
        # Put in matrix form
        buttons_matrix = np.array(buttons).T
        num_buttons = buttons_matrix.shape[1]
        c = np.ones(num_buttons)
        integrality = np.ones(num_buttons)
        bounds = Bounds(lb=0, ub=np.inf)
        constraints = LinearConstraint(buttons_matrix, joltage, joltage)
        result = milp(c, constraints=constraints, bounds=bounds, integrality=integrality)
        answer += result.fun
    return answer

part_two_example_answer = part_two(example_data)
part_two_answer = part_two(data)