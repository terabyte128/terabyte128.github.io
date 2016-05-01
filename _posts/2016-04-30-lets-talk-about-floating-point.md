---
layout: post
title: "Let's talk about floating point"
date: 2016-04-30 22:15:49
categories:
---

Ah, floating point: not just a swimming pool full of numbers!

You may or may not be familiar with the somewhat convoluted way that computers deal with non-integer numbers (for instance, $$1.25$$, or $$6.022 * 10^{23}$$). I'm not sure how you really would have ended up here without having searched for something like "floating point," so you probably already know at least a bit about how it works. But either way, I have a test on Monday, so I'm going to attempt to describe this standard as clearly as possible. (And in excruciating detail, woo!)

### Some background

Computers really don't have much to work with. Remember, everything eventually ends up as just 1's and 0's. This can make it difficult to represent things like, for instance, decimal points. This led to some, uh, *interesting* compromises with number representation.

The most obvious way to get around this lack of a decimal point is by just arbitrarily choosing a spot for it within a number. Suppose I wanted to represent the 16-bit binary number $$10101101.01010011$$ in computer memory. I could just say that the decimal point will always be in the middle (i.e. with 8 bits on either side), and store it as $$1010110101010011$$ with the implied point.

But it turns out that this doesn't work so well if, sticking with the 16-bit number example, I want to represent something with more than 8 bits of precision on either side. Using this fixed-point method, I can't represent any numbers larger than $$256$$ ($$2^8$$), or anything more precise than $$\frac{1}{256}$$ ($$2^{-8}$$). *And that's not even considering how to represent negative numbers*, which would take away even more precious bits. There must be a better way.


### Whatever floats your boat

And as it turns out, there is one! Aside from some very specific instances where you know exactly what kind of numbers you're dealing with, fixed-point turns out to not be all that useful. And everyone seemingly had their own unique way to deal with non-integer numbers, non of which were, of course, compatible. So in 1985, the **IEEE 754** standard was established to bring order to a scattered universe. And it might seem complicated at first, but bear with me for a bit, because it's really not as complex as it seems.


### Taking a cue from science

You're probably familiar with scientific notation. It's much handier to write $$6.022*10^{23}$$ than it is to write $$602200000000000000000000$$. They really mean the same thing, but in the first form, you can just see the number of digits that will be there after the decimal point, as opposed to actually needing to write them all down.

Floating point works in essentially the same way, except computers don't think in base 10, preferring instead to stick to binary. But let's start with a decimal example. I want to represent $$125$$ in scientific notation. Well that's pretty easy, just move the decimal place over twice to the left, and then multiply by $$100$$ (or $$10^2$$). Then I have:

\begin{align}
1.25 * 10^2
\end{align}

*Nice.* Turns out this also works in binary. First, convert $$125$$ to base 2: $$1111101$$. I'd like to end up with only a single number, $$1 \le n \lt 10$$, before the point. But remember, unlike decimal, the only number in binary for which this works is $$1$$ itself! $$1_2 + 1_2 = 10_2$$. So that makes it pretty easy. How many times will I have to move the point over in $$1111101$$ to end up with just a $$1$$ in front? Turns out it's $$6_{10} = 110_2$$ times. So I end up with:

\begin{align}
1.111101 * 10^{110}
\end{align}

But **watch out!** There's a subtle but important difference between this number in scientific notation and the one above it. The $$10^{110}$$ here, remember, is actually in base 2, and so each time I move the point over once, I'm multiplying by a power of 2, *not* a power of 10 as above.

Let's do another example. Suppose I want to represent $$16.25$$ in scientific notation, base-2. First I'll convert it into base-2 and leave the point as it is: $$10000.01$$. I'll just move the point over to the left $$4_{10} = 100_2$$ places, and end up with:

\begin{align}
1.000001 * 10^{100}
\end{align}

*Bada bing, bada boom.* This isn't so bad. That is, essentially, how computers deal with numbers like these -- with a couple of small twists.


### All together now

IEEE 754 specifies that certain parts of a floating-point *word* (that's just a fancy term for a specified number of bits) are allocated to specific areas of a floating-point number. There are 3 pieces (remember this is in binary, so we only have $$0$$ and $$1$$):

* The **sign bit**. We haven't talked about this before, but it's pretty much exactly what you'd expect. Remember, we still need a way to tell if a number is positive or negative. If the sign bit is $$0$$, the number is positive. If the sign bit is $$1$$, the number is negative. That's all <a href="#" title="Except this introduces a weird issue where you can have positive and negative 0, but let's not worry about that for now.">(mostly)</a>.  
* The **mantissa**, otherwise known as the **significand**. This sounds weird, but it's really just the original number with the point moved over appropriately. However, since in binary the digit before the point *must* be a one, we can just get rid of the most significant bit completely and implicitly say that we know it's still there.
* The **exponent**, which is simply the number by which we multiply the mantissa to arrive back at the original value.

All three of these pieces then just get squashed together into a certain size word -- 32 bits for a float, and 64 bits for a double.

Let's do this the best way: with another *exciting example.* Suppose I have a number, $$26.5$$. That's a nice-sounding number. I'd like to represent it as a 32-bit floating-point number. First, I'll convert it to binary: $$11010.1$$. Now, I'll move the point over $$4_{10} = 100_2$$ times to the left and end up with:

\begin{align}
1.10101 * 10^{100}
\end{align}

For a normal 32-bit `float`, the pieces are allocated the following number of bits:

 * Sign Bit: 1 bit
 * Exponent: 8 bits
 * Mantissa: 23 bits


Plenty of room for our small number. Let's see how it all goes together:

* Sign bit: This one's easy. The number is positive, so it's just $$0$$.
* Exponent: A bit more difficult, and this is a good time to bring up the idea of *bias*. Ideally we'd like to be able to multiply by negative powers of 2 as well as positive powers. This allows storage of really precise small numbers as well as really large numbers. But to do this, it will be necessary to have some way to represent a negative sign.  
The solution was to add a bias to the exponent, so that instead of only representing numbers from $$0$$ to $$2^n$$, where $$n$$ is the number of bits in the exponent, we can give up half the positive numbers to represent negative exponents as well. With an 8-bit exponent, the bias is $$127_{10}$$, or $$01111111_2$$. Great. So that means that the final exponent for the number above will be $$100 + 01111111 = 10000011$$.
* Mantissa: Exactly as shown above, except we just drop the leading 1 since it'll always be there, and end up with $$10101$$.

Then just pad the right side of the mantissa with zeroes (since the numbers are assumed to come right after the implied point, and are therefore "most significant"), and Bob's your uncle:

\begin{align}
0\ 10000011\ 10101000000000000000000
\end{align}

### A few notes

Some numbers can't be represented exactly in base-2, and computers aren't that great at inference, so you may get weird behavior when trying to use some floating-point numbers:

{% highlight swift %}
swift> 0.1 + 0.1
$R0: Double = 0.20000000000000001
{% endhighlight %}

This is because $$0.1$$ in binary is an irrational number $$0.000110011001100110011...$$, and eventually the computer will run out of bits when trying to precisely do arithmetic with it and have to round somewhere, causing unexpected output.

### And some special cases

There are a few numbers in floating-point representation that mean special things:

* All bits except sign bit are $$0$$: represents $$0$$. The sign bit can be either $$1$$ or $$0$$, meaning that technically floating point can have both $$+0$$ and $$-0$$, but they should evaluate to equal.
* If the exponent is all 1's, and the mantissa is all 0's, then the number represents $$\infty$$. Depending on the sign bit, this can be either $$+\infty$$ or $$-\infty$$.
* If the exponent is all 1's, and the mantissa is *not* all 0's, then the number represents `NaN`.

### Wrap-up

Well, if you're still with me at this point, hopefully I've helped you out a bit along the way. If you found this information helpful, or have more questions, feel free to <a href="/contact_me">shoot me an email</a>.

I used [MathJax](https://www.mathjax.org) to embed $$\LaTeX$$ into this webpage, in case you were curious :)

<script type="text/javascript" async
  src="//cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
