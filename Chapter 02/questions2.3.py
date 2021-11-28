import math
from math import cos, pi, sin, sqrt, tan
from matplotlib.patches import Polygon
from matplotlib.pyplot import grid
from vectors import length
from vectors import to_cartesian
from vector_drawing import draw
from vector_drawing import Polygon

# 2.2.27
# print(length((-1.34, 2.68)))

# 2.2.28
# tan(22) ~= 0.4

# 2.2.29
# length = 15, degrees = 37
# sine (37) = 0.6
# cosine (37) = 0.8
# 15 * 0.6 = 9 == b
# 15 * 0.8 = 12 == a
#  ~= (12, 9)

# 2.2.30
# length = 8.5
# theta = 125
# sin (125 d) = 0.819
# cos (125 d) = -0.574
# y = 6.9615
# x = -4.879

# 2.2.31
# sin (0) = 0
# cos (0) = 1
# sin (90) = 1
# cos (90) = 0
# sin (180) = 0
# cos (180) = -1

# 2.2.32
# d = 1
# print(sqrt(3)/2)
# print(1 * sin(pi/3))
# print((1/2)/1) # sin
# print((sqrt(3)/2)/1) # cos
# print((1/2)/(sqrt(3)/2)) # tan

# print(float(1/2.0))
# print(1 * cos(pi/3))

# print(sqrt((0.5) ** 2 + (sqrt(3)/2) ** 2)) # is 1

# 2.2.33
# d = 1

# print((sqrt(3)/2)/1) # sin
# print((1/2.0)/1) # cos
# print((sqrt(3)/2)/(1/2.0)) # tan

# 2.2.34
# print(cos((50.0/360.0) * 2 * pi)) # = 0.643
# this assumes that the length of the hypotenuse is 1
# therefore we just need to solve for x, x being the sine length.
# we can use the pythagorean theorem to solve for x.

# x = 1 ** 2 - 0.643 ** 2 
# print(x)
# print(sqrt(x))

# 2.2.35
# 1 radian = 57.296
# 116.57 in radians then would be 116.57 / 57.296
# y = 116.57 / 57.296
# print(y)
# print(tan(y))

# 2.2.36
# is 10*pi/6 positive or negative for sin and cos values?
# guess: 10/6 is about 1 2/3, so positive cos, but negative sin

# p = 10*pi/6
# print(p)
# print(sin(p))
# print(cos(p))

# 2.2.37
# polar_coords = [(cos(5*x*pi/500.0),2*pi*x/1000.0) for x in range(0,1000)]
# vectors = [to_cartesian(p) for p in polar_coords]
# draw(Polygon(*vectors, color=green))

# 2.2.38
# hypo = sqrt(13), x = -2, y = 3
# sin (theta) = 3 / sqrt(13) ~= 0.832, arccosine(0.832)
# cos (theta) = -2 / sqrt(13) ~= -0.554, arcsine(-0.554)
# arcosine, and arcine, and arctangent does not work here, math.atan2 works with coordinate points thus can work.
def to_polar(vector):
    x, y = vector[0], vector[1]
    angle = math.atan2(3, -2) # how you use the lib to get the angle
    return (length(vector), angle)

to_polar((-2, 3))

# 2.2.39
to_polar((1,1)) # (sqrt(2), pi/4)
to_polar((1,-1)) # (sqrt(2), -pi/4) # online is wrong, book is correct

# 2.2.40
mouth = [(-5,2), (-2,2), (-5,1)]
toe = [(0,-3), (-1,-4), (1,-4)]
tail = [(3,1), (6,4), (5,1)]

