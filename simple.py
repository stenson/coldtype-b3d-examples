from coldtype import *
from coldtype.blender import *

@b3d_animation(timeline=60)
def simple(f):
    return (StSt("CT", Font.ColdtypeObviously(), 500
        , wdth=f.e("eeio"))
        .align(f.a.r)
        .pen()
        .ch(b3d(lambda bp: bp
            .extrude(f.e("eeio", r=(0.25, 5))))))
