from aocd import get_data
import numpy as np
from scipy.cluster.hierarchy import DisjointSet

data = get_data(day=8,year=2025)
example_data = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

def parse_data(data):
    parsed_data = [[int(i) for i in row.split(',')] for row in data.split('\n')]
    return parsed_data

def all_distances(parsed_data):
    distances = []
    for i,(x,y,z) in enumerate(parsed_data):
        for j,(xx,yy,zz) in enumerate(parsed_data):
            if i<j:
                dist = np.sqrt((x-xx)**2+(y-yy)**2+(z-zz)**2)
                distances.append((dist, i, j))
        max_i = i
    return sorted(distances,key=lambda x:x[0]), max_i

def connect_number(all_distances,number_to_connect):
    ad_copy = all_distances.copy()
    ds = DisjointSet([])
    for i in range(number_to_connect):
        min_dist, left, right = ad_copy.pop(0)
        ds.add(left)
        ds.add(right)
        ds.merge(left, right)
    return ds

def part_one(data,number_to_connect):
    parsed_data = parse_data(data)
    ad, _ = all_distances(parsed_data)
    connected = connect_number(ad, number_to_connect)
    all_subsets = connected.subsets()
    subset_len = sorted([len(i) for i in all_subsets],reverse=True)
    answer = subset_len[0]*subset_len[1]*subset_len[2]
    return answer


def connect_all(all_distances, max_num):
    ad_copy = all_distances.copy()
    ds = DisjointSet([i for i in range(max_num+1)])
    done = False
    i = 0
    last_added = None
    while not done:
        min_dist, left, right = ad_copy.pop(0)
        last_added = (left,right)
        ds.merge(left, right)
        i += 1
        if i < 10:
            continue
        else:
            subset_len = len(ds.subsets())
            if subset_len == 1:
                done = True
    return last_added, ds

def part_two(data):
    parsed_data = parse_data(data)
    ad, max_num = all_distances(parsed_data)
    last_added, ds = connect_all(ad, max_num)
    answer = parsed_data[last_added[0]][0] * parsed_data[last_added[1]][0]
    return answer

part_one_example_answer = part_one(example_data,10)
part_one_answer = part_one(data,1000)

part_two_example_answer = part_two(example_data)
part_two_answer = part_two(data)