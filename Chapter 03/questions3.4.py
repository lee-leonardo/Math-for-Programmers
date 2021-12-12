# cross product outputs a vector, this vector can be used to compute the 2d area of two vectors.
# it is focused on measuring orientation in 3d space, as without orientation dimensionality loses meaning.
# it outputs area and direction.
# it is useful because it helps you understand the space you can see from a specific perspective.
def cross(u, v):
    ux, uy, uz = u
    vx, vy, vz = v
    return (uy*uz - uz*vy, uz*vx - ux*vz, ux*vy - uy*vx)

# 3.19
# a, c, d

# 3.20
# mirrored is a reversed orientation

# 3.21
print(cross((0,0,3), (0,-2,0))) # output: (6,0,0)
# x is supposedly pointed towards us.

# 3.22
print(cross((1,-2,1), (-6,12,-6))) # output: (-14,0,0)
# the vector length is supposedly zero...

# 3.23
# height is |v| * sin(theta)
# area is width * height.
# since we know in this example we are measuring based on an angle that we can treat the width as the origin line, thus ignore the angle there (cos(0) == 1)
# thus we can easily just calculate |u| * |v| * sin(theta)

# 3.24
print(cross((1,0,1), (-1,0,0))) # output: (0,-1,0)


# 3.25
u = (0,0,1)
print(cross(u, (1,2,3)))
print(cross(u, (-1,2,-3)))
print(cross(u, (1,-2,3)))

# 3.26
# mathematically perpendicular cancel out.
# so (u x v) * u and (u x v) * v both should cancel out
# (uy*uz - uz*vy, uz*vx - ux*vz, ux*vy - uy*vx) * (ux, uy, uz)
# (ux * (uy*uz - uz*vy) + uy * (uz*vx - ux*vz) + uz * (ux*vy - uy*vx)) 
# ((ux*uy*uz - ux*uz*vy) + (uy*uz*vx - uy*ux*vz) + (uz*ux*vy - uz*uy*vx)) 
# 0

# (uy*uz - uz*vy, uz*vx - ux*vz, ux*vy - uy*vx) * (vx, vy, vz)
# (vx * (uy*uz - uz*vy) + vy * (uz*vx - ux*vz) + vz * (ux*vy - uy*vx))
# ((vx*uy*uz - vx*uz*vy) + (vy*uz*vx - vy*ux*vz) + (vz*ux*vy - vz*uy*vx))
# 0
