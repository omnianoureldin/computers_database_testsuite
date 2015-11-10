#!/bin/bash
set -e

echo -e '\e[32m** Creating virtual environment ...\e[0m'
rm -rf venv
virtualenv venv
source venv/bin/activate

echo -e '\e[32m** Installing requirements ...\e[0m'
venv/bin/pip install -r requirements.txt
