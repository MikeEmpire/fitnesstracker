#!/bin/bash

read -r -p 'Package name: ' package

pip uninstall $package

pip freeze > requirements.txt

echo "Successfully uninstalled $package"
