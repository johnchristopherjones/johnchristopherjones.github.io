---
layout: post
title: How to add a new syntax highlighter to the Evernote ST3 package
tags: python, evernote, sublime text, published, share
notebook: Postach.io
---



I recently added FileMaker syntax highlighting to the Evernote package for Sublime Text 3.  Here's the quick version.

1.  Write your lexer as a pygments plugin.

    This is the hard part.  You'll need the [pygments documentation](http://pygments.org/docs/) to do this.  You can use my [FileMaker lexer](https://github.com/johnchristopherjones/FileMakerLexer) as a starting point, or you can use [my previous post](http://vorpal.club/my-quest-to-add-filemaker-calculations-to-pygments) as a guide.

    Don't forget to include the `__all__` variable in your lexer's module scope.

    Once you've got your pygments plugin put together you can use pygmentize generally.  But it takes a little more work to get it into the Evernote Sublime Text 3 package.

2.  Install the Evernote package from GitHub, not Package Control.

    You need to patch the installation of pygments inside the Evernote package, which you shouldn't try to do from the Package Control version.

    1.  If you've already installed the plugin, use package control to remove it.
    2.  Close Sublime Text.
    3.  On OS X Yosemite, open Terminal and run the following commands:

        ```bash
        $ cd "~/Library/Application Support/Sublime Text 3/Packages"
        $ git clone https://github.com/bordaigorl/sublime-evernote.git Evernote
        ```

    4. Restart Sublime Text and confirm that the Evernote package is working.

3.  Install `pygments` from source in the Evernote package.

    The `pygments` distributed with the Evernote package isn't the full repo that you need to add a new lexer.  You'll need some extras to install a new lexer.

    Nuke the included `pygments` module, download the current repo, and link the module subdirectory to where the Evernote package expects it.

    ```bash
    $ cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Evernote/lib/
    $ rm -r pygments
    $ hg clone http://bitbucket.org/birkenfeld/pygments-main pygments-main
    $ ln -s pygments-main/pygments pygments
    ```

4.  Incorporate the plugin into the pygments module in the Evernote <abbr title="Sublime Text 3">ST3</abbr> package.

    Incorporating the plugin is technically a little tricky, but it's very mechanical.

    1.  Copy your `lexer.py` to pygments with an original name.

        ```bash
        $ cd pygments-main/pygments/lexers/
        $ cp ~/Source/FileMakerLexer/filemakerlexer/lexer.py fmcalc.py
        ```

    2.  Recreate the map files for `pygments` to link your lexer.

        ```bash
        $ cd ../..
        $ make mapfiles
        ```

    4.  Copy an example file to `pygments-main/tests/examplefiles` for testing and run the pygments tests.

        ```bash
        $ cp ~/Source/FileMakerLexer/test_data/#.fmfn tests/examplefiles/filemaker_calculation.fmfn
        $ make test
        ```

5.  Close any tabs that use the Evernote package and then restart Sublime Text.

You should now be able to use your new lexer in fenced code blocks in the Evernote plugin.  That means fenced code blocks using GitHub-flavored MarkDown will upload to Evernote with syntax highlighting.  You won't see the syntax highlighting in Sublimte itself.

For example, the following MarkDown:

    ```filemaker
    Let ( $error = ErrorFmpGetLast ( "" ) ; "" )
    ```

now yields the following code block:

```filemaker
Let ( $error = ErrorFmpGetLast ( "" ) ; "" )
```
