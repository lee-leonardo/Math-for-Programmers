from draw3d import Segment3D, draw3d

# 3.27
# my initial thought was to create a list of points, and then create list of edges, and faces, but using the points is enough to draw the edges with a loop.

points = [(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)]
top = points[0]
bottom = points[3]
xy_plane = points[1:3] + points[4:]

edges = [
    [Segment3D(top, p) for p in xy_plane],
    [Segment3D(bottom, p) for p in xy_plane],
    [Segment3D(xy_plane[i], xy_plane[i+1%4]) for i in range(0,4)]
]

draw3d(edges)

# 3.28
# by determining the top or the bottom, it's just a matter of how you wish to loop. Just need to recognize which points are neighbors and create the edges to those.
