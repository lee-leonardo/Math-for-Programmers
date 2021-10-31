from matplotlib.patches import Polygon
from matplotlib.pyplot import grid
from vectors import length
from vector_drawing import draw
from vector_drawing import Points
from vector_drawing import Polygon

dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4), 
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3), 
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]

# 2.2.6

# u = (-2,0)
# v = (1.5,1.5)
# w = (4,1)

# u+v = (-0.5,1.5)
# v+w = (5.5,2.5)
# u+w = (2,1)
# u+v+w = (3.5,2.5)

# 2.2.7
def add(*vectors):
    return (sum(v[0] for v in vectors),sum(v[1] for v in vectors))

print(add((1,1), (-1,1), (1,-1)))

# 2.2.8
def translate(translationVector, vectors):
    return [add(translationVector, v) for v in vectors]


print(translate((1,1), [(0,0), (0,1,), (-3,-3)]))

# 2.2.9
# This is just a proof, explainable via the vector mathematics basic principal, and addition via the start being the end of another point.

# 2.2.10
# Hypothetical example.

# 2.2.11
def hundredDinos():
    translations = [(12*x, 10*y) 
        for x in range(-5,5)
        for y in range(-5,5)]
    dinos = [Polygon(*translate(t, dino_vectors))
        for t in translations]
    draw(*dinos, grid=None, axes=None, origin=None)

# hundredDinos()

# 2.2.12
# (3,-2) + (1,1) + (-2,-2)
# x = 3 + 1 + -2 >> |2|
# y = -2 + 1 + -2 >> |-3|
# therefore y, because 

# 2.2.13
# (-6,-6) (5,12)
# (-6,-6) >> (-6,0), (0,-6)
# (5,0), (0,12)

# 2.2.14
# length = 6, x = (1,0), find all possible coordinates
#  Pythagorean Theorem: C^2=A^2+B^2, 6^2 = 1^2 + b^2 => 36-1 = b^2, sqrt(35) e.g. ~5.9 from (1,0).
# combos: are all positive or negative 5.9

# 2.2.15
# this is cool, key is a function!
print(max(dino_vectors, key=length))

# 2.2.16
# w = (sqrt(2), sqrt(3))
# pi * w = (pi*sqrt(2), pi*sqrt(3))

# 2.2.17
def scale(s,v):
    return (s * v[0], s * v[1])

# 2.2.18
# a^2 + b^2 = c^2 <pythagorean theorem>
# |(a,b)| = c = sqrt(a^2+b^2) <vector represenation>
# if sa, sb then (sa,sb) <so applying the pythagorean theorem>
# |(sa,sb)| = sqrt((sa)^2 + (sb)^2) <vector rep of pythacorean theorem>
# |(sa,sb)| = sqrt(s^2*a^2 + s^2*b^2) <multiplicatively>
# ** = sqrt(s^2 * (a^2+b^2)) <multiplicatively>
# ** = |s| * sqrt(a^2+B^2) <move out of sqrt>
# ** = |s| * c

# 2.2.19
# u = (-1,1), v = (1,1)
# -1 < r < 1, -3 < s < 3
# r * u + s * v
# (-2,0) < r * u < (0,2)
# (-2,-2) < s * v < (4,4)
# extremes:
# (-4,-2),(2,4),(-2,0),(4,6)
# code that can work for this:
from random import uniform
u = (-1,1)
v = 1,1
def random_r():
    return uniform(-3,3)

def random_s():
    return uniform(-1,1)

possibilities = [
    add(scale(random_r(), u), scale(random_s(), v)) for i in range(0, 500)
]

draw(Points(*possibilities))