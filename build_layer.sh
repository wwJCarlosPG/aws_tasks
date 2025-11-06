#!/bin/bash
set -e

mkdir -p layer/python
pip install -r requirements.txt --platform manylinux2014_x86_64 --target layer/python --only-binary=:all: