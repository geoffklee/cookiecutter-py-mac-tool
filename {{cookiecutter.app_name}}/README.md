{{ cookiecutter.project_name }}
===============================

version number: {{ cookiecutter.version }}
author: {{ cookiecutter.full_name }}

Overview
--------

{{ cookiecutter.project_short_description }}

Installation / Usage
--------------------

Clone the repo:

    $ git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}.git
    $ python setup.py install

Or, build with autopkg:

    $ autopkg repo-add https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}/autopkg-recipe
    $ autopkg run {{cookiecutter.app_name}}.pkg

    
Contributing
------------

TBD

Example
-------

TBD
