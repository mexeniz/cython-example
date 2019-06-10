#!/bin/bash

# Copy source file
rm -rf build
mkdir build
cp -r src/myapi build

# Build module
cd build/myapi
python setup.py build_ext --inplace

# Clean build directory and all source files except __init__.py
rm -rf build
find . \( -name '*.c' \) -delete
find . \( -name '*.py' -and ! -name '__init__.py' \) -delete