# pyscaffold

An opinionated starter template for setting up a python 3.9+ package with a CLI.

## Customize for your project...

To customize for your own package:

1. Find and replace `pyscaffold` and replace with `yourproject` - or whatever you want to call it.
    - includes source code, tests, and the readme!
    - rename the `pyscaffold` project folder too
2. Follow the developer setup below!
3. Delete this section from your readme

AKA, the manual [cookiecutter](https://github.com/cookiecutter/cookiecutter)...

## Quickstart

Make sure you have python 3.9 available and on your path. Then:

```bash
# update pip
python -m pip install -U pip

# if it's local file...
pip install path/to/pyscaffold-0.0.1-py3-none-any.whl
# if it's on github somewhere...
pip install path/to/pyscaffold-0.0.1-py3-none-any.whl
# if it's on pypi
pip install pyscaffold

# test our CLI
pyscaffold --help
pyscaffold hello
pyscallold hello --name Andy
pyscaffold bottles -n 10
```

## Developer setup

```bash
# clone project
git clone git@github.com:shapiromatron/pyscaffold.git
cd pyscaffold

# create virtual environment and activate
python -m venv venv --prompt pyscaffold
source venv/bin/activate  # or venv\Scripts\activate on windows.

# install packages
python -m pip install -U pip
pip install -r requirements_dev.txt

# test local install
pyscaffold hello

# these should work on mac/linux/windows
make test   # run tests
make lint   # identify formatting errors
make format  # fix formatting errors when possible
make build  # build a python wheel
```

Github actions are setup to execute whenever code is pushed to check code formatting and successful tests. In addition, when code is pushed to the `main` branch, a wheel artifact is created and stored on github.
