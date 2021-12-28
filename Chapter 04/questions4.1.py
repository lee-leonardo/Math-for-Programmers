from vectors import add
from transforms import polygon_map, scale_by, compose
from draw_model import draw_model
from teapot import load_triangles
from scale_teapot import scale2
from scale_translate_teapot import translate1left


# 4.1
def translate_by(translation):
    def new_function(v):
        return add(translation, v)
    return new_function

# 4.2
draw_model(
    polygon_map(
        translate_by((0,0,-20)),
        load_triangles()
    )
)

# 4.3
draw_model(
    polygon_map(scale_by(0.5), load_triangles())
)

draw_model(
    polygon_map(scale_by(-1), load_triangles())
)

# 4.4
draw_model(
    polygon_map(compose(scale2, translate1left), load_triangles())
)

# 4.5
compose(scale_by(0.4), scale_by(1.5)) # will be 60%

# 4.6
def multiCompose(*args):
    def newFn(input):
        state = input
        for fn in args:
            state = fn(state)
        return state
    return newFn

# 4.7