#!/bin/bash
set -e

if [ -d "venv" ]
then
    echo 'Do you want to re-create venv? [Yy/Nn]'
    read yn
    if [[ "$yn" =~ ^(Y|y)$ ]]
    then
        echo -e '\e[32m** Creating venv ...\e[0m'
        rm -rf venv
        virtualenv venv
        source venv/bin/activate

        echo -e '\e[32m** Installing requirements ...\e[0m'
        venv/bin/pip install -r requirements.txt
    fi
else
        echo -e '\e[32m** Creating venv ...\e[0m'
        rm -rf venv
        virtualenv venv
        source venv/bin/activate

        echo -e '\e[32m** Installing requirements ...\e[0m'
        venv/bin/pip install -r requirements.txt

fi

echo -e '\e[32m** Running tests ...\e[0m'
venv/bin/nosetests --with-progressive tests/


