#!/bin/bash
REPO_PATH=$(pwd)

# Copy source file
echo "==> Copying source"
rm -rf build
mkdir build
cp -r src/myapi src/tests build

# Build module
echo "==> Building module"
cd build/myapi
python setup.py build_ext --inplace

# Testing 
echo "==> Run unit testing"
cd ${REPO_PATH}
pytest -sv build/tests

# Clean build directory and all source files except __init__.py
echo "==> Clean build directory"
cd ${REPO_PATH}/build
find . | grep -E "(build|__pycache__|\.pyc|\.pyo$|\.c$)" | xargs rm -rf
find myapi \( -name '*.py' -and ! -name '__init__.py' \) -delete