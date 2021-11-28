from vectors import to_cartesian
from vectors import to_polar

# 2.42
# write a rotate(angle, vectors)
def rotate(angle, vectors):
    polars = [to_polar(x) for x in vectors]
    return [to_cartesian(d, a + angle) for d, a in polars]
