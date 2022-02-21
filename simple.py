from coldtype import *
from coldtype.blender import *

@b3d_animation()
def simple(f):
    return (StSt("E", Font.ColdtypeObviously(), 500
        , wdth=f.e("eeio"))
        .align(f.a.r)
        .pen()
        .ch(b3d(lambda bp: bp
            .extrude(0.5))))
