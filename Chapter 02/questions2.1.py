from matplotlib.patches import Polygon
from matplotlib.pyplot import grid
from vector_drawing import draw
from vector_drawing import Points
from vector_drawing import Polygon

# 2.1.3 
dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4), 
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3), 
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]

# 2.1.4
draw(
    Points(*dino_vectors),
    Polygon(*dino_vectors)
)

# 2.1.5
draw(
    Points(*[(x,x**2) for x in range(-10,11)]),
    grid=(1,10),
    nice_aspect_ratio=False
)