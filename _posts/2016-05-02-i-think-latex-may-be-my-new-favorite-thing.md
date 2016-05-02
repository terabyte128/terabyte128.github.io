---
layout: post
title: "LaTeX may be my new favorite tool"
date: 2016-05-02 13:05:44
categories:
---

Let me start by saying that I'm not talking about latex, the rubber-like material. I'm talking about LaTeX (pronounced LATEK), the typesetting system. LaTeX is the preferred choice for those who have to write extended research papers, and for good reason: it provides a way to programmatically write really, *really* nice looking documents, including built-in functionality for equations. It's kind of like  HTML meets Microsoft Word-style output, but also better than both of those. Let me show you what I mean, using a cool online $$\LaTeX$$ library called [MathJax](https://www.mathjax.org).


### Equations
One of $$\LaTeX$$'s best features is its excellent equation formatting abilities. For instance, if I want to write some complex math formula, I can just type:

`$\int_{-3}^{7} 11x^2 + e^x + \pi\ dx$`

and I end up with:

$$\int_{-3}^{7} 11x^2 + e^x + \pi\ dx$$

*Nice!* So easy, and so pretty! Personally, I much prefer this type of layout to dealing with Word's "Equation Editor." Since $$\LaTeX$$ basically knows what I want, and it has built-in ideas for how math formulas should work, it can reliably generate nice-looking formulas without me needing to specify too much.

### Documents
Of course, it's good for much more than math. I've started to write out all my documents using $$\LaTeX$$ instead of word, because it **just works**<sup>TM</sup>, and it has nice layout features for documents beyond equations (including a citation editor - which I haven't personally used, but if it works like the rest of the language, I imagine it's pretty nice).

The idea behind the language is that it probably knows better than you do, how your documents should look, so it provides you with tools for certain types of formatting -- like title pages, sections, and subsections -- and then decides how to format the layout in a clear, consistent manner. But of course, if you're not satisfied, you can change things to your liking, it just takes a bit more effort. Still more fun than using something like Word, and probably with better results. For instance, I wrote my <a href="/Samuel_Wolfson_Resume.pdf">resume</a> in $$\LaTeX$$, and I really like the clear layout and formatting.

### Wrap-up

Now, this isn't intended to be a tutorial -- there are [plenty](https://www.latex-tutorial.com/) [of](www.andy-roberts.net/misc/latex/) [tutorials](https://www.tug.org/twg/mactex/tutorials/ltxprimer-1.0.pdf) [floating](https://en.wikibooks.org/wiki/LaTeX/Basics) [around](http://www.cs.cornell.edu/info/misc/latex-tutorial/latex-home.html) on the Internet. But if you're someone who frequently writes papers, or math proofs, and you don't already have experience with $$\LaTeX$$, then I highly recommend checking it out. As with all things, there is a bit of a learning curve, but there are plenty of resources and I think you'll eventually find it to be a much more satisfying experience than a program like Microsoft Word.

For reference, I've been using [texmaker](http://www.xm1math.net/texmaker/), which has built-in shortcuts to common commands, and [MacTeX](http://tug.org/mactex/).

<script type="text/javascript" async
  src="//cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
