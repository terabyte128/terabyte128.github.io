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
	else:
		print("Selection is invalid.")
		show_greeting()
	
	print("** Process finished!")
	show_greeting()

show_greeting()