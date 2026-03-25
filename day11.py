from aocd import get_data
from functools import cache
import networkx as nx

data = get_data(day=11,year=2025)
example_data = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

def parse_data(data):
    DG = nx.DiGraph()
    for row in data.split('\n'):
        left,right = row.split(': ')
        all_right = right.split(' ')
        DG.add_node(left)
        for r in all_right:
            DG.add_edge(left, r)
    return DG

def part_one(data):
    parsed_data = parse_data(data)
    paths = nx.all_simple_paths(parsed_data,'you','out')
    answer = 0
    for path in paths:
        answer += 1
    return answer

part_one_example_answer = part_one(example_data)
part_one_answer = part_one(data)

example_data_part_two = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

#Thanks to Jonathan Paulson, @jonathan_paulson, for the idea behind this code
@cache
def traverse_graph(graph, x, passed_dac, passed_fft):
    if x == 'out':
        return 1 if passed_dac and passed_fft else 0
    else:
        paths = 0
        for edge in graph[x]:
            new_dac = passed_dac or edge == 'dac'
            new_fft = passed_fft or edge == 'fft'
            paths += traverse_graph(graph, edge, new_dac, new_fft)
        return paths

def part_two(data):
    parsed_data = parse_data(data)
    answer = traverse_graph(parsed_data, 'svr', False, False)
    return answer

part_two_example_answer = part_two(example_data_part_two)
part_two_answer = part_two(data)