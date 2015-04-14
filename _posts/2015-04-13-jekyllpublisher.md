---
layout: post
title: "Jekyll Publisher"
date: 2015-04-13 22:53:13
categories: publisher jekyll automate
---

Jekyll Publisher automates a bunch of the mundane tasks inside Jekyll and let you spend more of your time writing content, instead of trying to remember the exact date, time and syntax of every page!

It's intended to be used with GitHub Pages for committing & pushing updates, but it can create posts and pages as well.

<pre>
~ Jekyll Publisher ~

1. Create new page
2. Create new blog post
3. Commit changes
4. Publish changes
5. Commit & publish to GitHub
6. Exit

Enter selection:
</pre>

Source code is below. It's essentially a wrapper for everything I wrote about in my last post. You can [download it here.](https://raw.githubusercontent.com/terabyte128/terabyte128.github.io/master/JekyllPublisher.py)

{% highlight python %}
#!/usr/bin/python
# -*- coding: ascii -*-

import sys
import subprocess
import time

def show_greeting():
	print("~ Jekyll Publisher ~\n")
	print("1. Create new page")
	print("2. Create new blog post")
	print("3. Commit changes")
	print("4. Publish changes")
	print("5. Commit & publish to GitHub")
	print("6. Exit")

	try:
		choice = int(raw_input("\nEnter selection: "))
	except ValueError:
		print("Selection is not an integer.")
		show_greeting()
		
	process_choice(choice)
	
def new_page():
	title = raw_input("Enter a new page name: ")
	filename = title.replace(" ", "_").lower() + ".md"
	
	f = open(filename, 'w')
	
	f.write("---\n")
	f.write('layout: page\n')
	f.write('title: "' + title + '"\n')
	f.write('permalink: /' + title.replace(" ", "_").lower() + '/\n')
	f.write('---\n\n')
	
	f.close()

def new_blog_post():
	timestr = time.strftime("%Y-%m-%d")
	
	title = raw_input("Enter a new post title: ")
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
	
def make_commit():
	message = raw_input("Enter commit message: ")
	subprocess.call(['git', 'add', '.'])
	subprocess.call(['git', 'commit', '-m', message])
	
def publish_commit():
	subprocess.call(['git', 'push'])
	
def process_choice(choice):
	if choice == 1:
		new_page()
	elif choice == 2:
		new_blog_post()
	elif choice == 3:
		make_commit()
	elif choice == 4:
		publish_commit()
	elif choice == 5:
		make_commit()
		publish_commit()
	elif choice == 6:
		print("Goodbye!")
		exit()
	else:
		print("Selection is invalid.")
		show_greeting()
	
	print("\n** Process finished!\n")
	show_greeting()

show_greeting()
{% endhighlight %}