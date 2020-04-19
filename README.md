# python-repo-template

[![githubactions](https://github.com/actions/typescript-action/workflows/build-test/badge.svg)](https://github.com/kyhau/python-repo-template/actions)
[![travis](https://travis-ci.org/kyhau/python-repo-template.svg?branch=master)](https://travis-ci.org/kyhau/python-repo-template)
[![codecov](https://codecov.io/gh/kyhau/python-repo-template/branch/master/graph/badge.svg)](https://codecov.io/gh/kyhau/python-repo-template)


This is a template repository that you can use to quickly create a python application that can be built, tested, and
released as an internal python module.

Support Python 3.7, 3.8, 3.9.

**Use**

- [Travis CI](https://travis-ci.org/)
- [GitHub Actions](https://github.com/actions)
- [tox](https://tox.readthedocs.io/en/latest/)
- [codecov](https://codecov.io/) 
- [black](https://github.com/psf/black)
- [bump2version](https://github.com/c4urself/bump2version)
- [flake8](https://gitlab.com/pycqa/flake8)
- [Mypy](https://github.com/python/mypy)

## Setting up a new repository from this template

Create a directory and pull all the files in this template.

```
mkdir new_repo_name
cd new_repo_name
git init
git pull https://github.com/kyhau/python-repo-template
```

## Create virtual env and install dependencies 

**Linux**

```bash
virtualenv -p python3.8 env
. env/bin/activate
pip install -e .
```

**Windows**
```
virtualenv -p C:\Python38\python.exe env
env\Scripts\activate
pip install -e .
```

## Run Black, then run pytest, codecov, mypy and flake8 with Tox

```
pip install -r requirements-build.txt

# Autoformat code following most of the rules in PEP 8
black --line-length=79 module/

# Run pytest, codecov, mypy and flake8 with Tox
tox -r
```


## Version-bump your application or module with [bump2version](https://github.com/c4urself/bump2version)

Examples

    # e.g. 1.2.3.dev0 -> 1.2.3
    bumpversion --allow-dirty --commit --tag release

    # e.g. 1.2.3 -> 1.2.4.dev0
    bumpversion --commit patch

    # e.g. 1.2.3.dev0 -> 2.0.0.dev0
    bumpversion --commit major

    # e.g. 1.2.3.dev0 -> 1.3.0.dev0
    bumpversion --commit minor
    
    # e.g. 1.2.3.dev0 -> 1.2.4.dev0
    bumpversion --commit patch

    # e.g. 1.2.3.dev0 -> 1.2.3.dev1
    bumpversion --commit dev

    # e.g. 1.2.3.dev0 -> 1.2.3
    bumpversion --dry-run --list release