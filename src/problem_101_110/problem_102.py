'''
Created on May 22, 2014

@author: anuvrat
'''

from collections import namedtuple
import math

filename = '/Users/anuvrat/git/project-euler-python/resource/problem_102_input.txt'

Point = namedtuple('Point', ['x', 'y'])

def area_of_triangle(p1, p2, p3):
    return math.fabs((p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)) * 0.5)

origin = Point(0, 0)
interior_origin_triangles = 0
with open(filename) as f:
    for line in f:
        coordinates = map(int, line.split(','))
        
        p = []
        for i in xrange(0, 6, 2): p.append(Point(coordinates[i], coordinates[i+1]))
        
        area = []
        for i in xrange(3): area.append(area_of_triangle(p[i], p[(i+1) % 3], origin))
        
        area_triangle = area_of_triangle(p[0], p[1], p[2])
        
        if sum(area) == area_triangle: interior_origin_triangles += 1

print(interior_origin_triangles)