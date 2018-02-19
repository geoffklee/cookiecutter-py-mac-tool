from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '{{cookiecutter.version}}'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='{{cookiecutter.app_name}}',
    version=__version__,
    description='{{cookiecutter.project_short_description}}',
    long_description=long_description,
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}',
    download_url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}/tarball/v' + __version__,
    license='Apache Software License',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 2',
    ],
    keywords='mac',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='{{cookiecutter.full_name}}',
    install_requires=None,
    dependency_links=None,
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pylint'],
    author_email='{{cookiecutter.email}}',
    entry_points={
        'console_scripts': [
           '{{cookiecutter.app_name}} = {{cookiecutter.app_name}}.__init__:main'
          ]
    },
)
