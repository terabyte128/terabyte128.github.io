---
layout: post
title: An Update to Jekyll Publisher
categories: 
date: 2018-10-07 15:42:45 +0200
---

I've started using Jekyll again, and I remembered the tool for automatically creating pages and publishing blogs that I posted a while back. I've re-written it so that it uses command-line arguments instead of requiring interaction at each step. Now it's much faster to use (and can be automated, if you wanted to do that for some reason). You can find the new version of it [as a Gist on GitHub](https://gist.github.com/terabyte128/b9f2d8eec082c2987170f2399e0a1443).

Usage information is available with the `--help` argument. Supported commands are `newpage` for creating new static pages, `newblog` for new blog posts, and `git` for committing and publishing changes to GitHub Pages.
