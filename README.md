- Install a Python3.9

- Make a python virtual environment
    - macOS
        - using blender's python:
        - using a standard python install:
            - `python3.9 -m venv venv` (non-m1 mac computer)
            - `python3.9-intel64 -m venv venv` (m1 mac computer)
    - windows (in git bash)
        - `alias b3d_python="/c/Program\ Files/Blender\ Foundation/Blender\ 3.0/3.0/python/bin/python.exe"`
        - `b3d_python -m venv venv`

- ⚠️ Activate the environment ⚠️
    - macOS
        - `source venv/bin/activate`
    - windows
        - `source venv/Scripts/activate`

- Install coldtype into the virtual environment
    - `python3.9 -m pip install "coldtype[viewer]" --upgrade`

- Verify coldtype is installed
    - `coldtype demo`

- Install coldtype into the Blender python installation
    - macOS
        - `/Applications/Blender.app/Contents/Resources/X.XX/python/bin/python3.9 -m pip install "coldtype[viewer]" --upgrade`
    - windows:
        - `b3d_python -m pip install "coldtype[viewer]"

- Run example in 2D mode:
    - `coldtype nowin3d.py`

- Run example in 2D+3D mode:
    - `coldtype nowin3d.py -p b3d`

- Run example in 3D mode:
    - `coldtype nowin3d.py -p b3dlo`