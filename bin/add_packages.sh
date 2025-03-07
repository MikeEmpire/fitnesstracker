#!/bin/bash

read -r -p 'Enter Package names (space-separated): ' package

pip install $package

pip freeze >requirements.txt

echo "Successfully installed $packages"
