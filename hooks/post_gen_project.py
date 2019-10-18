import sys
import subprocess
import requests
""" Post hook to initialise a new git repository, and connect up a remote 
    if desired. We try to be careful to exit 0 for non-fatal errors, as this
    can all be done manually if it fails for some reason
"""

print("Initialising git repository")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

resp = None

try:
    repo = 'https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}'
    resp = requests.get(repo)

except requests.RequestException as err:
    # Maybe there's no network connection - no biggie!
    print(("Failed to check for a remote git repository ({})."
           " No problem though - you're otherwise good to go.").format(err))
    sys.exit(0)

if resp.status_code != 200:
    print("Can't find a git repo at {} - not attempting to initialise git".format(repo))
    sys.exit(0)

print("Git repo exists at: {}".format(repo))

answer = None

while answer not in ['y', 'n']: 
    answer = input("We found a remote git repository which looks like it matches this project.\nDo you want to add it as a git remote? (y/n)")

if answer == 'n':
    print("Not adding a git remote")
    sys.exit(0)
elif answer == 'y':
    print("Adding a git remote at {}".format(repo))    

    try:    
       subprocess.check_call(['git', 'remote', 'add', 'origin', repo])

    except subprocess.CalledProcessError as err:
       print("Failed to add a git remote({}). You're otherwise good to go.".format(err))
       sys.exit(0)

    print("Repository initialised - `git push --set-upstream origin master` to push your initial commit") 
