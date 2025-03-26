# pyscaffold

An opinionated starter template for setting up a python 3.13+ package with a CLI.

NOTE: this project is unrelated to the excellent [PyScaffold](https://pypi.org/project/PyScaffold/) project. This repo will likely not be published to pypi, and handles a much smaller and more narrow use case. Apologies in advance for the confusion in naming.

## Customize for your project...

To customize for your own package:

1. Search & replace `pyscaffold` and replace with `yourproject` (or whatever you want to call it).
    - includes source code, tests, and this readme!
    - rename the `pyscaffold` project and test folder too
2. Review pyproject.toml; change `authors`, `classifiers`, `project.urls`, etc.
3. Follow the "Developer setup" section below
4. Update this readme! Delete this section, edit quickstart guide, etc.

This is a manual [cookiecutter](https://github.com/cookiecutter/cookiecutter). This was done intentionally; keeping it a manual job is nice for testing because it makes it easier to ensure that our github actions work as expected. Maybe one day we will switch to using cookiecutter.

## Quickstart

Install [uv](https://docs.astral.sh/uv/) and make it available and on your path. Then:

```bash
# update and install
uv sync

# test our CLI
uv run pyscaffold --help
uv run pyscaffold hello
uv run pyscaffold hello --name Andy
uv run pyscaffold bottles --num 20
```

NOTE: this is a standard python package that you can install in other ways; we suggest using uv to make things easier, but you can always use standard pip and manage a virtual environment however you prefer.

## Developer setup

Make sure you have uv available on your path. Then:

```bash
# clone project
git clone git@github.com:shapiromatron/pyscaffold.git
cd pyscaffold

# create virtual environment and activate
uv sync --all-extras

# run assorted commands
uv run poe --help
uv run poe test    # run tests
uv run poe lint    # identify formatting errors
uv run poe format  # fix formatting errors when possible
uv run poe build   # build a python wheel
```

Github actions are set up to execute whenever code is pushed to check code formatting and successful tests. In addition, when code is pushed to the `main` branch, a wheel artifact is created and stored on github.
