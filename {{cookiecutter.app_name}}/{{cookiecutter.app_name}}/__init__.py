# Copyright 2018 {{cookiecutter.full_name}}
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The {{cookiecutter.app_name}} tool"""
import argparse

VERSION = "{{cookiecutter.version}}"
DESCRIPTION = """This is the {{cookiecutter.app_name}} tool"""

def main():
    """Main function - do useful stuff here!"""
    args = process_args()

    # Now do stuff!
    assert args

def process_args(args=False):
    """Process any commandline arguments"""
    parser = argparse.ArgumentParser(description=DESCRIPTION,
                                     version=VERSION)
    args = parser.parse_args(args)
    return args

if __name__ == "__main__":
    main()
