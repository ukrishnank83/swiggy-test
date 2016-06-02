#!/bin/bash
echo "Install Python Virtual Environment(y/n)"
read venv
if [ $venv = "y" ]; then
     sudo apt-get install python-virtualenv
fi

source test/bin/activate
