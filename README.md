# python-repo-template

[![Build Status](https://travis-ci.org/kyhau/python-repo-template.svg?branch=master)](https://travis-ci.org/kyhau/python-repo-template)
[![codecov](https://codecov.io/gh/kyhau/python-repo-template/branch/master/graph/badge.svg)](https://codecov.io/gh/kyhau/python-repo-template)

This is a template repository that you can use to quickly create a python application that can be built, tested, and
released as an internal python module.

Support Python 3.6 and 3.7.

**Use**

- [Travis CI](https://travis-ci.org/)
- [tox](https://tox.readthedocs.io/en/latest/)
- [codecov](https://codecov.io/) 
- [bump2version](https://github.com/c4urself/bump2version)

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
virtualenv env
. env/bin/activate
pip install -e .
```

**Windows**
```
virtualenv env
env\Scripts\activate
pip install -e .
```

## Run pytest with Tox

```
pip install -r requirements-build.txt
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