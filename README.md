- Install a Python3.9

- Make a python virtual environment
    - macOS
        - `python3.9 -m venv venv` (non-m1 mac computer)
        - `python3.9-intel64 -m venv venv` (m1 mac computer)

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

- Run example in 2D mode:
    - `coldtype nowin3d.py`

- Run example in 2D+3D mode:
    - `coldtype nowin3d.py -p b3d`

- Run example in 3D mode:
    - `coldtype nowin3d.py -p b3dlo`