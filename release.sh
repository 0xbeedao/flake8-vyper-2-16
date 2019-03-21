#!/bin/sh

PROD_STRING="production"

ENV="$1"
if [ "$1" != "$PROD_STRING" ]; then
    ENV="test"
fi

if [ -z "$PYTHON_BIN" ]; then
    if [ -z "$VIRTUAL_ENV" ]; then
        PYTHON_BIN="/usr/bin/python"
    else
        PYTHON_BIN="python"
    fi
fi

echo "Building $ENV release $SB_VERSION..."

echo "Cleaning dist directory..."
rm -rf dist/*

echo "Building wheel distribution..."
$PYTHON_BIN setup.py sdist bdist_wheel

if [ $ENV == "$PROD_STRING" ]; then
    echo "Uploading to PyPi..."
    twine upload dist/*
else
    echo "Uploading to TestPyPi..."
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
fi
