from math import cos, acos, pi, sqrt
from vectors import to_polar

def length(v):
    return sqrt(sum([coord ** 2 for coord in v]))

# dot product for 2d
def dot2d(u, v):
    return sum([coord1 * coord2 for coord1, coord2 in zip(u,v)])

# dot product of form |u| * |v| * cos(theta)
def dot2dLenCos(lu, lv, degrees):
    return lu * lv * cos(degrees * pi / 180)

#  thea from dot product cos
def thetaDot2dCos(u, v, degrees):
    return acos(
        dot2d(u, v) / (length(u) * length(v))
    )

# 3.11
u = (1,2)
v = (4,2)
w = (-4,1)

a = dot2d(u, v)
b = dot2d(u, w)
c = dot2d(v, w)
print(a,b,c)

# u*w > v*w > u*w

# 3.12
u = (-1,-1,1)
v = (1,2,1)
print(sum([a * b for a,b in zip(u,v)])) # should be -2, because 1*-1 + -1*2 + 1*1 = -2, therefore greater than 90 degrees

# 3.13
# this is just a proof
# s * u or s * v is equal to  (s * u1, s * u2) and (s * v1, s * v2)
# u * v is (u1 * v1, u2 * v2)
# using the multiplicative property, you can assume that s(u) * v == u * s(v) == s(u * v)

# 3.14
# u * u == u ** 2
# example: u = (2,2), u * u then is (2 ** 2, 2 ** 2) or (4,4).
# length is sqrt(x ** 2 + y ** 2)
# dot product is u*v = ux * uv + uy * vy. if v = u then you are multiplying it by itself, and adding the x and the y. Meaning that the value is the square of the length which is the value of the square root of the dot product

# 3.15
# be lazy, just use (0,3), (0,7) for p1. p2 use u=(0, -3), v=(0, 7) , u=(0, 3), v=(0, -7), u=(3,0) v=(-7,0)
# use dot to calculate
print(dot2d((0,3), (0,7)))
print(dot2d((0,-3), (0,7)))
print(dot2d((0,3), (0,-7)))
print(dot2d((-3,0), (7,0)))

# check page 102 for for loop version.

# 3.16
print(dot2dLenCos(3.61, 1.44, 101.3))

# 3.17
u = (3,4)
v = (4,3)

a, x = to_polar(u)
b, y = to_polar(v)
print(x-y, y-x)

# you can also use thetaDot2dCos to get the value (but with the 3d formulation)
deg = acos(sum([x * y * z for x,y,z in zip(u,v)]) / (length(u) * length(v)))
print(deg)

# 3.18
u = (1,1,1)
v = (-1,-1,1)

deg = (sum([x * y * z for x,y,z in zip(u,v)])/ length(u) * length(v))
print(deg)
