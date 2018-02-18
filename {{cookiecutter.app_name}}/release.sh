#!/bin/bash
# Use this script to generate a new relese
# This script will:
#
# 1. Check that the local source tree is up to date 
# 2. Run tests
# 3. Bump the version number as requested (major, minor, or patch)
# 4. Create a new tag and commit it to the local git tree 
# 5. That's all.

# Bail immediately if anything fails
set -Eeuo pipefail

release_level=${1:-none}

if [ "${release_level}" != "major" ] &&\
   [ "${release_level}" != "minor" ] &&\
   [ "${release_level}" != "patch" ]
then
   echo "Specify major, minor or patch"
   exit 1
fi

pip install bumpversion

git checkout master

git pull origin master

python setup.py test

# Bump a new version - this creates a new git tag
new_version="$(bumpversion --list patch | awk -F '=' '/new_version/ {print $2}')"

# Pat on the back
echo "###################################################################"
echo "# Congratulations! You've created version ${new_version}. It hasn't"
echo "# yet been pushed to the git origin server, though."
echo "#"
echo "# Now, you probably want to run:"
echo "#"
echo "# git push origin v${new_version}"
echo "###################################################################"
