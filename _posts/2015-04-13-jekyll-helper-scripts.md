---
layout: post
title: "Jekyll helper scripts"
date: 2015-04-13 14:04:31
categories: jekyll helper scripts
---

I've written a few helper scripts in Python to make using and publishing with Jekyll and GitHub pages easier. The first one creates blog post skeletons with the current date and time, and using a title given as an argument.

{% highlight python %}
#! /usr/bin/python

import time
import subprocess
import sys

timestr = time.strftime("%Y-%m-%d")

if len(sys.argv) != 2:
    print("Usage: ./create_post.py [page name]")
    exit()

title = sys.argv[1]

filename = "_posts/" + timestr + "-" + title.replace(" ", "-").lower() + ".md"

datetimestr = "date: " + time.strftime("%Y-%m-%d %H:%M:%S")

f = open(filename, 'w')

f.write("---\n")
f.write('layout: post\n')
f.write('title: "' + title + '"\n')
f.write(datetimestr + "\n")
f.write('categories: \n')
f.write('---\n\n')

f.close()
{% endhighlight %}

The other script allows committing and pushing with one command, which is particularly useful for a project like this, where changes don't necessarily need as much review as a conventional GitHub project.

{% highlight python %}
#! /usr/bin/python

import sys
import subprocess

args = sys.argv

if len(args) != 2:
    print("Usage: ./commit_and_push.py [commit message]")
	exit()

print("adding all files...")
subprocess.call(['git', 'add', '.'])

print("committing...")
subprocess.call(['git', 'commit', '-m', args[1]])

print("pushing...")
subprocess.call(['git', 'push'])

print("done!")
{% endhighlight %}

**Hope you find these scripts useful!**