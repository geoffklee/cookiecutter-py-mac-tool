#!/bin/bash

# ###################################################
# This script can be used to test the cookiecutter. 
# If all goes well, it will:
#
#   * Cut a new cookie called 'mymacadmintool'
#   * Commit to git (nb the repo must exist)
#   * Make a new release (v0.0.2)
#   * Commit the release
#   * Use autopkg to build a macOS package
#
#####################################################
set -euo pipefail

echo "CookieCuttting..."
cookiecutter --no-input https://github.com/gkluoe/cookiecutter-py-mac-tool

cd mymacadmintool

echo "Initing git repo.."
git init 

echo "Adding files..."
git add .

echo "Committing..."
git commit -m 'Initial commit'

echo "Adding remote..."
# NB, this repository has to exist, and be empty.
git remote add origin https://github.com/gkluoe/mymacadmintool.git

git push origin master

./release.sh patch

git push origin v0.0.2

autopkg run -d autopkg-recipe mymacadmintool.pkg
