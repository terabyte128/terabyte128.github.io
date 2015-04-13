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
