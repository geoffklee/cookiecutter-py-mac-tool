"""The {{cookiecutter.app_name}} tool"""
import argparse

VERSION = "{{cookiecutter.version}}"
DESCRIPTION = """This is the {{cookiecutter.app_name}} tool"""

def main():
    """Main function"""
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
