---
layout: post
title: How to gracefully handle external scripts in FileMaker
tags: filemaker, applescript
notebook: Postach.io
---
If you use FileMaker for a little while—say, an afternoon—you have run into one
of two problems I run into basically every day:

  1.  I want to get my data into or out of FileMaker.
  2.  I want to manipulate my data and FileMaker calculations are clearly the wrong tool.

Quite often the transformation I want to do is trivial in AppleScript, a shell script, Python, Ruby, or even a little JavaScript.
However, if you've tried to use AppleScript or shell scripts in FileMaker you've probably run into a huge problem.

*How do you get your data into these scripts and maintain your sanity?*

You have basically two obvious choices for constructing those scripts.

  1.  Use a "calculated" script for the `Perform AppleScript` script step.
  2.  Use a "native" script for the `Perform AppleScript` script step.

That's bad enough.  If you use a "native" AppleScript you kind of have to hard code your data into the calculation.
That's probably useless.
If you use a "calculated" AppleScript you have to wrap everything in escapes and quotes and append "¶" to everything.
And that's just the AppleScript.
You should also `try`/`catch` your exceptions of course.
Then, if you want to throw a little Python in there holy hell do you quickly run into scape sequences that look like ``\\\\'\\\\"\\\\\\\\'`.
No.
*No.*

**No.**

I'm going to show you a great way to deal with this problem that will let you write your scripts *completely without escapes and concatenation*, if that's what you want.
You'll be able to execute *python* scripts on your database records without difficulty.
