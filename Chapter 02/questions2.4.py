from math import pi

from vector_drawing import draw
from vectors import to_cartesian
from vectors import to_polar
from vectors import translate
from vectors import rotate

# 2.42
# write a rotate(angle, vectors)
# def rotate(angle, vectors):
#     polars = [to_polar(x) for x in vectors]
#     return [to_cartesian(d, a + angle) for d, a in polars]

# 2.43
# write regular_polygon(n) that returns the cartesian coordinates of an n sided polygon
def regular_polygon(n):
    angle = (2 * pi) / n
    return [to_cartesian((1, angle * i)) for i in range(0,n)]

# 2.44
# dino_vector translate by (8,8) then rotate by 5*pi/3, what about vv?
dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4), 
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3), 
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]

draw(
    dino_vectors,
    translate((8,8), to_cartesian(rotate(5 * pi / 3, to_polar(dino_vectors)))),
    to_cartesian(rotate(5 * pi / 3, to_polar(translate((8,8), dino_vectors))))
)

# no othey are not the same