from math import sin, cos, pi
from draw3d import draw3d, Arrow3D

def add(*vectors):
    by_coordinate = zip(*vectors)
    coordinate_sums = [sum(coords) for coords in by_coordinate]
    return tuple(coordinate_sums)

# 3.3
# (4,0,3) + (-1,0,1) = (3,0,4)

# 3.4
vectors1 = [(1,2,3,4,5), (6,7,8,9,10)]
vectors2 = [(1,2), (3,4), (5,6)]
# zip(*vectors1) = [(1,6), (2,7), (3,8), (4,9), (5,10)], length = 5
# zip(*vectors2) = [(1,3,5), (2,4,6)], length = 2

# 3.5
vs = [(sin(pi*t/6), cos(pi*t/6), 1.0/3) for t in range(0,24)]

current = (0,0,0)
arrows = []

for next in vs:
    next_sum = add(current, next)
    arrows.append(Arrow3D(current, next_sum, color=blue))
    start = next_sum

print(arrows)
draw3d(*arrows)

# 3.6
def scale(scalar, vector):
    return tuple(scalar * coords for coords in vector)

# 3.7
u = (1,-1,-1)
v = (0,0,2)

print(add(u, scale(0.5, add(v, scale(-1, u)))))

# 3.8
# (1,1) = sqrt(2) <= sqrt(1 ** 2 + 1 ** 2)
# (1,1,1) = sqrt(3) <= sqrt(1 ** 2 + 1 ** 2 + 1 ** 2)
# (1,1,1,1) = 2 <= sqrt(4) <= sqrt(1 ** 2 + 1 ** 2 + 1 ** 2 + 1 ** 2)

# 3.9

