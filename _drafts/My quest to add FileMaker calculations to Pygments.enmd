---
title: My quest to add FileMaker calculations to Pygments
tags: python, sublime text, evernote, published
notebook: Postach.io
---

This is not a short step-by-step howto, which I'll get to in a follow-up post.  This is a journal of my adventure adding a new lexer to a special Pygments installation.

I work in FileMaker a lot. I use Sublime to edit my FileMaker calculations thanks to the wonderful [Evernote package for Sublime Text 3](https://sublime.wbond.net/packages/Evernote).

However, I want to add syntax highlighting for FileMaker calculations to my blog. To make that work, I need to create a Pygments lexer for FileMaker calculations. From the Pygments docs I was pretty sure I could work out the lexer—no problem. But, where do I put the code? I was pretty stumped by this, until I found [Jonas Lundberg's excellent guide](http://www.catchmecode.com/2013/03/custom-syntax-in-pygments.html).

### How to start a pygments lexer

To add syntax highlighting for a language to pygments, I have to create a new "lexer".  A lexer is used to parse a language into labeled tokens.  Ultimately, the tokens are highlighted according to the labels.  So, step 1 is to make a new lexer.  Pygments will use the lexer and do the rest of the work after that.

### Step 1: Create a project folder for the new pygments lexer

I made a folder called FileMakerLexer with the following structure:

    FileMakerLexer/
    ├── README.md
    ├── filemakerlexer
    │   ├── __init__.py
    │   └── lexer.py
    └── setup.py

The `README.md` isn't required, but I plan to push this to github.

`__init__.py` can be totally empty.  Its existence tells python that `filemakerlexer` is a module.

`setup.py` helps make an egg, which helps plug the plugin into pygments while developing it.  I mostly copied `catchmecode.com` here:

```python
from setuptools import setup, find_packages

setup (
    name = 'filemakerlexer',
    package = find_packages(),
    entry_points =
    """
    [pygments.lexers]
    filemakerlexer = filemakerlexer.lexer:FileMakerLexer
    """,
)
```

The `entry_points` portion of this file will hook the egg into the pygments module as a plugin.  Pygments defines these [entry points](http://pygments.org/docs/plugins/).

I can't recall ever creating a `setup.py` before.  It seems a little spooky.  Suddenly I can run `python setup.py` and it has all sorts of package management options for my module.  Looking carefully at the above code, I see that I actually import the setup() function from setuptools and then call the setup() function with some options.  It's the setup() function that does all the magic.  It knows how to parse command line arguments and everything.

`lexer.py` is the actual lexer code.  This is where the fun goes.

### Step 2: Make a really basic lexer

A really basic "Hello, World!" kind of lexer would be the following:

```python
import re

from pygments.lexer import RegexLexer
from pygments.token import *

class FileMakerLexer(RegexLexer):
    name = 'FileMaker'
    alias = 'fmcalc'
    filenames = ['*.fmcalc', '*.fmfn']
    tokens = {
        'root': [
            (r'\s+', Text),
        ]
    }
```

The above lexer subclasses the RegexLexer (which lets you use regular expressions for your lexer).  It defines the name of the lexer and some ways of describing the kinds of files that contain this language.  Finally, it defines a single 'Text' token for the 'root' state, which is the state the lexer starts in.  Your lexer can switch states if you need to control which tokens are acceptable at any given time in a way that doesn't work in regex.

Now that the skeleton module is in place, it needs to be plugged it into pygments to try it out.  This is the spooky part I really needed Jonas's guide for.  The following command links my development directory into my python distribution, allowing me to hack on my code and see the changes using regular python.  I'd probably use `virtualenv` if I had more experience with it.

```bash
$ sudo python setup.py developer
```

Now I can hack away on my lexer.py and run pygmentize against any test code I've got.  I'm at a bit of a loss as to how to write sane unit tests for this.  Instead, I just visually inspected the HTML renering of various files using a script like the following.

```bash
$ pygmentize -f html -O full,encoding=utf-8,style=monokai test_data/script.fmscript > /tmp/test.html && open /tmp/test.html
```

I bashed on my `lexer.py` until I was satisfied, [constantly referenceing the pygments docs](http://pygments.org/docs/lexerdevelopment/#adding-and-testing-a-new-lexer), and eventually arrived at [what I published on GitHub](https://github.com/johnchristopherjones/FileMakerLexer).

Once I'm happy with the lexer, if I don't need it globally available, I can uninstall it.

```bash
$ sudo python setup.py develop --uninstall
```

### Step 3: Install the Evernote ST3 package from GitHub instead of Package Control

Up until now, I've just been making a lexer plugin.  I wrote the lexer as a plugin so my code would be testable, redistributable, and to create a clean development environment.  Now I need to get my lexer into the pygments module that's installed *inside the Evernote package for Sublime Text*.  Luckily adding a new lexer to pygments is described [in the pygments documentation](http://pygments.org/docs/lexerdevelopment/#adding-and-testing-a-new-lexer).

The particulars of installing my lexer inside the `pygments` module inside the Evernte package are a little different—at least up front.  The author of the Evernote package, [Emanuele D'Osualdo](https://github.com/bordaigorl), was very helpful here.

The first caveat is that I can't (sanely) do it from the version of the plugin installed through Package Control.  The source code is compressed and it's a bit messy to un-package the package.  Instead, I should use the GitHub repository.

If the Evernote plugin was already installed via Package Control, use Package Control to remove it.

Explicitly close any Evernote tabs, then close Sublime Text.

On OS X Yosemite, open Terminal and install Evernote from GitHub:

```bash
cd "~/Library/Application Support/Sublime Text 3/Packages"
git clone https://github.com/bordaigorl/sublime-evernote.git Evernote
```

Restart Sublime Text and confirm that the Evernote package is working.  It may lag a bit at first as source gets interpretted for the first time.

### Step 4: Hack pygments in the Evernote ST3 package

Next, I need to dive into the pygments python module inside the Evernote package.  I'll be trying to figure out the [pygments docs](http://pygments.org/docs/lexerdevelopment/#adding-and-testing-a-new-lexer) here.  I need to "create a new module for your lexer class" in the `pygments/lexers` folder.  So:

```bash
$ cd Evernote/lib/pygments
$ cd lexers
$ cp ~/Source/FileMakerLexer/filemakerlexer/lexer.py fmcalc.py
```

Next, make sure the lexer is known outside of the module.  The documentation says “All modules in the `pygments.lexers` specify `__all__`.”  This means I'm missing an __all__ module-scope variable in lexer.py fmcalc.py.  Oops.  I need to add this line to my lexer.py under the top level of my module:

```python
__all__ = ['FileMakerLexer']
```

And I need to re-copy my `lexer.py` and then "rebuild the lexer mapping".
:

```bash
$ cp ~/Source/FileMakerLexer/filemakerlexer/lexer.py fmcalc.py
$ make mapfiles
make: *** No rule to make target `mapfiles'.  Stop.
```

There's no `Makefile` in here, anywhere.  This isn't a developer distribution of pygments.  Crap.

### Step 5: Detour—install pygments into the Evernote package from source

Let's try just replacing the pygments folder outright.  Thanks to git, I can always `git reset --hard` if I make a total hash of everything.

```bash
$ cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Evernote/lib/
$ rm -r pygments
$ hg clone http://bitbucket.org/birkenfeld/pygments-main pygments
-bash: hg: command not found
```

I don't have mercurial.  Why would I have mercurial?  Love the project, but it lost DVCS war.  Well, no hard feelings.  I'm still installing it with `brew`.

```bash
$ brew install hg
```

Try again:

```bash
$ hg clone http://bitbucket.org/birkenfeld/pygments-main pygments
```

Success?  The repo definitely downloaded correctly, but now I've lost all my highlghting in the Evernote package.

That's because the Evernote package's pygments is basically the `pygments` subfolder of the `pygments-main` repo.  I broke pygments by doing this.  I need to handle this a little differently.  I'm not too confident with mercurial, so step #1 is scorched earth.

```bash
$ rm -r pygments
$ hg clone http://bitbucket.org/birkenfeld/pygments-main pygments-main
$ ln -s pygments-main/pygments pygments
```

SUCCESS!  I've got the pygments repo in `pygments-main` and the Evernote package using the `pygments` subdirectory, and my syntax highlighting is working again.  Now I've got my `Makefile` in `pygments-main`.  Actually, the current pygments appears to have *lot* more languages than the version that came with the Evernote package, so maybe I've come out ahead.

### Step 6: Back to patching pygments

Copy our previously-updated lexer.py into the pygments repo:

```bash
$ cd pygments-main/pygments/lexers/
$ cp ~/Source/FileMakerLexer/filemakerlexer/lexer.py fmcalc.py
```

Now let's try that Makefile.

```bash
$ cd ../..
make mapfiles
(cd pygments/formatters; python _mapping.py)
pygments.formatters.bbcode
pygments.formatters.html
[…]
=== 14 formatters processed.
(cd pygments/lexers; python _mapping.py)
pygments.lexers.actionscript
[…]
=== 355 lexers processed.
```

Looks good.  Next, I store an example file with the proper extension (defined earlier in lexer.py) in `pygments-main/tests/examplefiles`.  I'll use #.fmfn from filemakerstandards.org's github repo.

```bash
cp ~/Source/FileMakerLexer/test_data/#.fmfn tests/examplefiles/filemaker_calculation.fmfn
```

According to the docs, I can try it out now.

```bash
$ ./pygmentize -O full -f html -o /tmp/example.html tests/examplefiles/filemaker_calculation.fmfn
env: python2: No such file or directory
```

Really?  *Sigh.*  I've got no good reason not to do this, I guess:

```bash
sudo ln -s /usr/bin/python2.7 /usr/bin/python2
```

OK.  Let's try again:

```bash
$ ./pygmentize -O full -f html -o /tmp/example.html tests/examplefiles/filemaker_calculation.fmfn
$ open /tmp/example.html
```

Great!  Looking good.

For the last step, I run `make test` to make sure the tokenized text matches the input text.  This can fail if regular expressions aren't correctly tokenizing every character.  Missed whitespace is one of the most common sources of errors.

```bash
$ make test
nose is required to run the Pygments test suite
make: *** [test] Error 1
```

Alrighty then.  Nose is a unit test package I haven't installed yet.  Simple enough.

```bash
$ sudo pip install nose
Downloading/unpacking nose
[…]
```

Let's try `make test` again:

```bash
$ make test
Pygments 2.1a0 test suite running (Python 2.7.6)...
.........[…]
```

This takes a long time and appears to stall partway through, but it eventually completes in 116 seconds, skipping 8 tests, no failures.

Okay.  Let's try a little FileMaker syntax highlighting.  Close all Evernote tabs in Sublime and restart Sublime Text.

```fmcalc
/* An expression I like to use to capture and clear error state in scripts */
Let ( [ $error = ErrorFmpGetLast ( "" ) ] ; "" )
```

SUCCESS!  I AM THE BEST!  EVER!  AT THIS!  EVENTUALLY!

Unfortunately my lexer is a little slow, which slows down saving notes to Evernote, but I can improve that later.