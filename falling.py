from coldtype import *
from coldtype.blender import *

tl = Timeline(90)

@b3d_runnable()
def setup(bw:BpyWorld):
    BpyObj.Find("Cube").delete()
    BpyObj.Find("Camera").locate(0,0,20).rotate(0,0,0)

    with (bw.deletePrevious(materials=False)
        .render_settings(samples=32, canvas=Rect(1080, 1080))
        .timeline(tl)
        .rigidbody(3, 300)
        ):
        (BpyObj.Cube("Floor")
            .scale(x=10, y=10, z=0.2)
            .applyScale()
            .rigidbody("passive", friction=0.5, bounce=0.15)
            .material("cube"))

@b3d_renderable(reset_to_zero=1)
def falling(r):
    return (StSt("ABC", Font.MutatorSans(), 500, tu=0)
        .align(r)
        .mapv(lambda i, p: p
            .tag(f"glyph_{i}")
            .ch(b3d(lambda bp: bp
                .extrude(0.3)
                .convertToMesh()
                .rigidbody(friction=0.5, bounce=0)
                , dn=True
                , zero=True))
            .ch(b3d_post(lambda bp: bp
                .locate_relative(z=23)))))
