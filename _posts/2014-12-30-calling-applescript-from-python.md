---
layout: post
title: Calling AppleScript from Python
tags: published, applescript, python
notebook: Postach.io
---

In my work I frequently have cause to call AppleScript from one language or vice versa.

I've tried various methods to call AppleScript from Python and they all work to some extent, but I recent sumbled across [Dr. Drang's method](https://www.leancrew.com/all-this/2013/03/combining-python-and-applescript/).  This is ridiculously simple and works for about roughly 90% of everything I need it for.

It's pretty simple.  Basically, you just call `osascript` with the `subprocess` module, but it uses `stdin` and `stdout` to pass the AppleScript to and from `osascript` for you.  This neatly takes care of most of your polyglot problems.  If you need to embed a value in an AppleScript string, there's a convenient `asquote` Python function to safely embed a Python string inside AppleScript.  This takes care of most of the remaining polyglot problems.

```AppleScript
import subprocess

def asrun(ascript):
    "Run the given AppleScript and return the standard output and error."
    osa = subprocess.Popen(['osascript', '-'],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    return osa.communicate(ascript)[0]

def asquote(astr):
    "Return the AppleScript equivalent of the given string."
    astr = astr.replace('"', '" & quote & "')
    return '"{}"'.format(astr)
```

I like it.
