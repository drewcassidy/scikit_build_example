import sys

try:
    from skbuild import setup
except ImportError:
    print(
        "Please update pip, you need pip 10 or greater,\n"
        " or you need to install the PEP 518 requirements in pyproject.toml yourself",
        file=sys.stderr,
    )
    raise

from setuptools import find_packages

setup(
    name="scikit_build_example",
    version="0.0.1",
    description="a minimal example package (with pybind11)",
    author="Henry Schreiner",
    license="MIT",
    packages=find_packages(),

    # uncommenting this throws an error that doesnt exist with setuptools setup()
    # "error: package directory '//scikit_build_example' does not exist"
    # package_dir={"": "."}, 

    include_package_data=True,
    cmake_install_dir=".",
    python_requires=">=3.6",
)
