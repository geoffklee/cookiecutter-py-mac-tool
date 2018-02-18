CookieCutter Python-Mac-Admin-Tool 
=============================

A minimal cookiecutter template for a python tool, with a focus on deployment to macOS.

[cookiecutter](https://github.com/audreyr/cookiecutter)
Inspired by: [cookiecutter-pipproject](https://github.com/wdm0006/cookiecutter-pipproject.git)

Goals
-------

The goal of this template is to provide a quick and simple starting point for macOS admins who want to quickly write,
test and release a simple tool, and keep on top of release management after that. 

The template provides:

 * Basic skeleton for a python commandline tool
 * Testing with pytest
 * Versioning with bumpversion
 * Scripted release management
 * An autopkg template (the only macOS specific thing about it) 

It's deliberately minimal and is supposed to provide a more robust and scalable alternative to just bashing out a few lines one day, and realising you have a sprawling Cthulu of code the next!
 
Using the template
----------------------

##### Clone the template #####

    $ pip install cookiecutter
    $ cookiecutter https://github.com/gkluoe/cookiecutter-python-macadmin-tool.git

You will be asked about your basic info (name, project name, app name, etc.). This info will be used in your new project.
 
##### Add some code #####

The file `projectname/__init__.py` is set up so that you can add some arguments to the `process_args()` function, and then do something with them in `main()`.

That's really all there is to it!

##### Add some tests #####

The template is configured to be used with `pytest`. Any function named test_\*() in any file named test_\*.py inside the 'tests' folder will be collected and run as a test.

Included are 2 sample tests, which:

 1. Run your project against pylint (*test_lint()*)
 2. Check that the version number reported by the tool matches the version number in setup.py (*test_version()*)

##### Run the tests #####
    $ python setup.py test

##### Make a release #####
Once you're happy with your functionality, you can make a release. First, you'll need to make sure the code is committed to a git repo:

    $ git init .
    $ git remote add origin https://github.com/[you]/[projectname].git
    $ git add .
    $ git push origin master
 
Once you've done this once, you can run the release script:

    $ ./release.sh

This creates a new tag and commits it locally. You'll then want to push the release to your git server:

    $ git push origin [new version]

And then, you probably want to build a package for deployment. The directory `autopkg-recipe` contains an autopkg recipe which you could either copy to your recipes repo, or use directly, like so:

    $ autopkg run --verbose -d autopkg-recipes [project].pkg
    
You'll end up with a package to install your tool to `/usr/local/bin`. The tool is a wrapper script which uses the functionality in your `__init__.py` file.

Contributing
--------------

Issues/Pull requests welcome. I'm particularly keen for this documetation to be helpful to newcomers, so suggestions for modifications are really appreciated.

License
---------

Apache licensed.

