from aocd import get_data
import numpy as np
import shapely as sh
from collections import namedtuple

data = get_data(day=9,year=2025)
example_data = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

point = namedtuple('Point',['x','y'])
edge = namedtuple('Edge',['fx','fy', 'tx', 'ty'])

def parse_data(data):
    points = []
    for i in data.split('\n'):
        x,y = i.split(',')
        points.append(point(int(x),int(y)))
    return points

def area(pt1, pt2):
    return (np.abs((pt1.x-pt2.x))+1)*(np.abs((pt1.y-pt2.y))+1)

def all_areas(parsed_data):
    areas = []
    for i, pt1 in enumerate(parsed_data):
        for j, pt2 in enumerate(parsed_data):
            if i < j:
                areas.append((area(pt1,pt2),i,j))
    return sorted(areas,reverse=True)

def part_one(data):
    parsed_data = parse_data(data)
    areas = all_areas(parsed_data)
    answer = areas[0][0]
    return answer

part_one_example_answer = part_one(example_data)
part_one_answer = part_one(data)

####################PART TWO FOLLOWS####################
def sort(a,b):
    if a < b:
        return a,b
    else:
        return b,a

def part_two(data):
    parsed_data = parse_data(data)
    poly = construct_polygon(parsed_data)
    answer = 0
    for i in range(len(parsed_data)-1):
        for j in range(i+1, len(parsed_data)):
            start_pt = parsed_data[i]
            end_pt = parsed_data[j]
            minx, maxx = sort(start_pt.x, end_pt.x)
            miny, maxy = sort(start_pt.y, end_pt.y)
            check_poly = construct_square_poly(minx,maxx,miny,maxy)
            if sh.within(check_poly, poly):
                check_area = area(start_pt,end_pt)
                if check_area > answer:
                    answer = check_area
    return answer

def construct_square_poly(minx, maxx, miny, maxy):
    polygon = sh.Polygon([(minx,miny),(minx, maxy),(maxx,maxy),(maxx,miny)])
    return polygon

def construct_polygon(parsed_data):
    coords = [(p.x,p.y) for p in parsed_data]
    polygon = sh.Polygon(coords)
    return polygon

part_two_example_answer = part_two(example_data)
part_two_answer = part_two(data)