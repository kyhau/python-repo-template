# python-repo-template

[![githubactions](https://github.com/kyhau/python-repo-template/workflows/Build-Main/badge.svg)](https://github.com/kyhau/python-repo-template/actions)
[![travisci](https://img.shields.io/travis/kyhau/python-repo-template.svg?label=Travis%20CI&logo=travis&style=flat-square)](https://travis-ci.org/kyhau/python-repo-template)
[![codecov](https://codecov.io/gh/kyhau/python-repo-template/branch/main/graph/badge.svg)](https://codecov.io/gh/kyhau/python-repo-template)
[![CodeQL](https://github.com/kyhau/python-repo-template/workflows/CodeQL/badge.svg)](https://github.com/kyhau/python-repo-template/actions/workflows/codeql-analysis.yml)


This is a template repository that you can use to quickly create a python application that can be built, tested, and
released as an internal python module.

Support Python 3.7, 3.8, 3.9, 3.10, 3.11.

**Use**

- [GitHub Actions](https://github.com/actions)
- [CodeQL](https://codeql.github.com) is [enabled](.github/workflows/codeql-analysis.yml) in this repository.
- [Dependabot version updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates) is [enabled](.github/dependabot.yml) in this repository.
- [Snyk](https://github.com/snyk/actions) is enabled in this repository.
- [Travis CI](https://travis-ci.org/)
- [black](https://github.com/psf/black)
- [bump2version](https://github.com/c4urself/bump2version)
- [codecov](https://codecov.io/)
- [flake8](https://gitlab.com/pycqa/flake8)
- [Mypy](https://github.com/python/mypy)
- [tox](https://tox.readthedocs.io/en/latest/)

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
virtualenv -p python3.10 env
. env/bin/activate
pip install -e .
```

**Windows**
```
virtualenv -p C:\Python310\python.exe env
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
