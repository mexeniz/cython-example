#!/bin/bash
REPO_PATH=$(pwd)
PACKAGE_NAME=myapi

# Copy source file
echo "==> Copying source files"
rm -rf build
mkdir build
cp -r src/${PACKAGE_NAME} src/tests build

# Build module
echo "==> Building modules"
cd build/${PACKAGE_NAME}
python setup.py build_ext --inplace

# Clean build directory and all source files except __init__.py
echo "==> Clean build directory"
cd ${REPO_PATH}/build
find . | grep -E "(build|__pycache__|\.pyc|\.pyo$|\.c$)" | xargs rm -rf
find ${PACKAGE_NAME} \( -name '*.py' -and ! -name '__init__.py' \) -delete

# Testing 
echo "==> Run unit testing"
cd ${REPO_PATH}
pytest -sv build/tests

if [[ $? -eq "0" ]]; then
    # Previous command run successfully.
    echo "==> Passed testing, Archive a package"
    cd ${REPO_PATH}/build
    tar cvfz ${PACKAGE_NAME}.tar.gz ../requirements.txt ${PACKAGE_NAME}/*
fi