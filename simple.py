from coldtype import *
from coldtype.blender import *

@b3d_runnable(playback=B3DPlayback.KeepPlaying)
def setup(bw:BpyWorld):
    BpyObj.Find("Cube").delete()
    bw.cycles(32, False, Rect(1080, 1080))

@b3d_animation(timeline=60)
def simple(f):
    return (StSt("CT", Font.ColdtypeObviously(), 500
        , wdth=f.e("eeio"))
        .align(f.a.r)
        .pen()
        .tag("letters")
        .ch(b3d(lambda bp: bp
            .extrude(f.e("eeio", r=(0.1, 1))))))
