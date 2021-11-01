# flake8-vyper

Flake8 wrapper to support Vyper.  This is forked from the original project at https://github.com/mikeshultz/flake8-vyper by @0xbeedao for Yearn.

*Note:* Since Vyper ASTs are strict, this package only works for Vyper 0.2.16.

## Install

Locally, preferably set up a Virtualenv.
    cd flake8-vyper-2-16
    python -m venv .
    python setup.py install
    
    python flake8_vyper.py [options] file1 [file2 ...]

Pip

    pip install git+https://github.com/0xbeedao/flake8-vyper-2-16

After install

    flake8-python-2-16 [options] file [file2 ...]

Example:
    flake8-python-2-16 --tee --filename *vy

## Configuration

You can use all the same CLI options as flake8, but config should be done in the `flake8-vyper`
section to prevent conflicts.  Here's an example `tox.ini` for a project with python and vyper:

    [flake8]
    exclude = .git,__pycache__,build
    max-line-length = 100
    filename = *.py

    [flake8-vyper]
    exclude = .git,__pycache__,build
    max-line-length = 100
    filename = *.vy
