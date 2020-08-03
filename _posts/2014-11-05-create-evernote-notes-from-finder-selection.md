---
layout: post
title: Create Evernote Notes from Finder Selection
tags: published, applescript, finder, evernote
notebook: Postach.io
---

[Adapted from a post to the Evernote Forums on 2013-12-15](https://discussion.evernote.com/topic/49309-create-evernote-notes-from-finder-selection/)_

I used to save articles I found on the web as PDFs and threw them into a folder. I also saved text files, images, and various sundry clips. I have archives going back to the late 90s in one digital form or another.

These days I use Evernote for such things and old content has become harder to locate or harder to even remember that it exists. So, I decided to import it into Evernote.

Evernote makes this *sort of* easy. You can actually just drag files onto Evernote and create notes that way. That's fine for recent stuff. However, one way I simplify my Evernote organization is to [use the creation and modification date of notes](https://www.jamierubin.net/2013/01/29/going-paperless-a-closer-look-at-how-i-organize-my-notes-in-evernote/), like [Evernote Ambassador Jamie Todd Rubin](https://www.jamierubin.net/going-paperless/). So, I wanted a couple of things:

  1. One note should be created for each file.
  2. Each note should be named after the filename.
  3. Each note should have the creation and modification timestamp of the original file.
  4. Each note should store the original path in its "source URL" field.

One of the things I really like about using a Mac is [AppleScript](https://developer.apple.com/library/mac/documentation/AppleScript/Conceptual/AppleScriptLangGuide/AppleScriptLanguageGuide.pdf). Not the language itself, which is twisted and wrong, but the capabilities it provides. I use AppleScript professionally so I've become extremely familiar with it. It's a little like becoming familiar with the One Ring.

Anyway, what AppleScript *really* lets you do is create missing features—especially inter-application features—for applications. I used AppleScript to create a feature for Finder so that I can import my current Finder selection into Evernote, one note per file. As a visual aid, it also tags the files “Evernote”.

```AppleScript
-- Create new notes in a notebook with this name
property importNotebook : "Inbox"

-- Save the Finder selection
tell application "Finder" to set selectedFiles to (selection)

repeat with f in selectedFiles
    -- For each item in the Finder selection
    -- Capture the file's metadata...
    tell application "Finder"
        set f to document file (f as alias)

        set creationDate to creation date of f
        set modificationDate to modification date of f
        set sourceUrl to URL of f
    end tell

    -- ... and create a new note with the file and its metadata
    tell application "Evernote"
        set filepath to POSIX path of (f as text)
        set newNote to create note title (name of f) from file (filepath as POSIX file) notebook importNotebook
        set creation date of newNote to creationDate
        set modification date of newNote to modificationDate
        set source URL of newNote to sourceUrl
    end tell

    -- Really hairy tagging in Mavericks.  Tags the files as Evernote and "Green".
    do shell script "xattr -w com.apple.metadata:_kMDItemUserTags '(\"Evernote\\n2\")' " & quoted form of (POSIX path of (f as alias))
    tell application "Finder" to set label index of file (f as alias) to item 4 of {2, 1, 3, 6, 4, 5, 7}
end repeat
```


Once I'd written this script, I could just select the files I wanted to import and run the script. In Finder, the files would receive the green “Evernote” tag, and in Evernote they would show up with their original filename as the title, their original file path as the source URL, and the creation and modification timestamp of the original file.

For a quick script I would create a [Keyboard Maestro](https://www.keyboardmaestro.com/) macro, but I actually created [an Automator Service](https://dl.dropboxusercontent.com/u/10516852/Add%20to%20Evernote%20with%20file%20date.zip) so the feature would show up in the context menu in Finder when I right-click on files. Just extract the archive and double-click the Automator service to install it in OS X 10.9 (“Mavericks”) and up. You can also set a keyboard shortcut through Keyboard Preferences for any menu item, including services you create with Automator.
