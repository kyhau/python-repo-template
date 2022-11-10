import os

from setuptools import find_packages, setup

base_dir = os.path.dirname(__file__)
__author__ = "kyhau"
__email__ = "virtualda@gmail.com"
__title__ = "module"
__version__ = "1.0.0.dev0"
__summary__ = "This package creates a framework for python packages to be built."
__uri__ = "https://github.com/kyhau/python-repo-template"

__requirements__ = []

__entry_points__ = {
    "console_scripts": ["new_module = module.main:main",],
}

__long_description__ = ""
try:
    # Reformat description as PyPi use ReStructuredText rather than Markdown
    import pypandoc
    __long_description__ = pypandoc.convert_file(os.path.join(base_dir, "README.md"), "rst")
except (ImportError, IOError, OSError) as e:
    print("long_description conversion failure, fallback to using raw contents")
    import io
    with io.open(os.path.join(base_dir, "README.md"), encoding="utf-8") as f:
        long_description = f.read()

CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3 :: Only",
]

setup(
    author=__author__,
    author_email=__email__,
    classifiers=CLASSIFIERS,
    # data_files parameter is only required for files outside the packages, used in conjunction with the MANIFEST.in
    data_files=[("", ["CHANGELOG.md"]),],
    description=__summary__,
    entry_points=__entry_points__,
    install_requires=__requirements__,
    long_description=__long_description__,
    name=__title__,
    # For data inside packages can use the automatic inclusion
    #   include_package_data = True,
    # or the explicit inclusion, e.g.:
    #   package_data={ "package_name": ["data.file1", "data.file2" , ...] }
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.7",
    url=__uri__,
    version=__version__,
    zip_safe=False,
)
