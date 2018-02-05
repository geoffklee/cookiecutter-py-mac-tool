# Sample Test running pylint

import subprocess

def test_lint():
    try:
        subprocess.check_output(["pylint", "{{cookiecutter.app_name}}/__init__.py"])
    except subprocess.CalledProcessError as error:
        print(error.output)
        print("test_lint() failed.")
        assert False

 

