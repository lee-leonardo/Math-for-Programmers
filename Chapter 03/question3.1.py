from draw3d import draw3d
from draw3d import Points3D
from draw3d import Segment3D

# 3.1
# uhhh what.

# 3.2
# vertices = [
#     (1,1,1), (1,1,-1), (1,-1,-1), (-1,-1,-1),
#     (-1,1,1), (-1,-1,1), (-1,1,-1), (1,-1,1),
# ]
# edges combines two of the verticies for 12
pm = [1,-1]
vertices = [
    (x,y,z) for x in pm
            for y in pm
            for z in pm
]
edges = [
    ((1,y,z), (-1,y,z)) for y in pm for z in pm
] + [
    ((x,1,z), (x,-1,z)) for x in pm for z in pm
] + [
    ((x,y,1), (x,y,-1)) for x in pm for y in pm
]

draw3d([
    Points3D(*vertices, color=blue)
    *[Segment3D(*edge) for edge in edges]
])
 