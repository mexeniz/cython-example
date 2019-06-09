#!/bin/bash

# Copy source file
rm -rf build
mkdir build
cp -r src/myapi build

# Build module
cd build/myapi
python setup.py build_ext --inplace