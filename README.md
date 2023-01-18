Here are some examples of what you can do with Coldtype + Blender.

### Getting started

First off, you’ll need a virtual environment.

The easiest and best way to create a virtual environment to use with Coldtype & Blender is to use the Python that's embedded in your copy of Blender. This is a little unconventional, but the `b3denv` package makes it easy to access and use Blender’s embedded Python outside of Blender.

Here are the steps to do it. (Note: the first `pip` call shouldn’t be in a virtual environment; b3denv is made to work with all versions of Blender, and if you already have it installed system-wide, you can skip that first step.)

- `pip install b3denv`
- `$(b3denv bpy) -m venv venv`
- `source venv/bin/activate` (or `source venv/Scripts/activate` on Windows)
- `pip install "coldtype[viewer]" -U`
- `coldtype -p b3dlo simple.py`