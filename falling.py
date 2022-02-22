from coldtype import *
from coldtype.blender import *

tl = Timeline(90)

@b3d_runnable()
def setup(bw:BpyWorld):
    with (bw.deletePrevious()
        .timeline(tl)
        .rigidbody(3, 300)
        ):
        (BpyObj.Find("Plane")
            .rigidbody("passive", friction=0.5, bounce=0.15))

@b3d_renderable(reset_to_zero=1)
def falling(r):
    return (StSt("ABC", Font.MutatorSans(), 500, tu=0)
        .align(r)
        #.t(5, 85)
        .mapv(lambda i, p: p
            .tag(f"glyph_{i}")
            .ch(b3d(lambda bp: bp
                .extrude(0.3)
                .convertToMesh()
                .rigidbody(friction=0.5, bounce=1)
                , dn=True
                , zero=True))
            .ch(b3d_post(lambda bp: bp
                .locate_relative(z=23)))))
