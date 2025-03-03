#!/usr/bin/env bash
# build.sh
set -o errexit

# ติดตั้ง build dependencies ที่จำเป็น
pip install --upgrade pip
pip install wheel setuptools
pip install -r requirements.txt