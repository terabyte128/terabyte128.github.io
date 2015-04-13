#! /usr/bin/python

import sys
import subprocess

args = sys.argv

if len(args) != 2:
    print("Usage: ./commit_and_push.py [commit message]")

else:
    print("adding all files...")
    subprocess.call(['git', 'add', '.'])

    print("committing...")
    subprocess.call(['git', 'commit', '-m', args[1]])

    print("pushing...")
    subprocess.call(['git', 'push'])
    
    print("done!")
