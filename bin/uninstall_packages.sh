#!/bin/bash

read -r -p 'Enter package names to uninstall (space-separated): ' packages

pip uninstall -y $packages

pip freeze >requirements.txt

echo "Successfully uninstalled $package"
