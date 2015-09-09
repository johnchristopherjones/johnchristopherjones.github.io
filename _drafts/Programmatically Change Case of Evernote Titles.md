---
title: Programmatically Change Case of Evernote Titles
tags: ["published", "applescript", "evernote"]
notebook: Postach.io
---

[JaperCaper on the Evernote forums had a problem](https://discussion.evernote.com/topic/49538-programmatically-change-case-of-note-titles/). JaperCaper imported 700+ PDFs into Evernote. The document titles were title case, but Evernote brought them in all lower-case. JaperCaper needed a fix.

Evernote has a <strike>great</strike>_good_ AppleScript API. It also has APIs for almost every language, but those SDKs are a little overkill for this task.

AppleScript itself has some weaknesses, like string processing. So, to make up for that we insert a little Python magic in our AppleScript to get the job done.

The following code will transform all selected notes to UPPERCASE.
    
    
```AppleScript
tell application "Evernote"
    -- Set the notes you want to rename here.
    -- Just getting every selected note
    set notesToRename to selection

    -- Looping over Evernote notes.  Calling the current note "n".
    repeat with n in notesToRename
        set noteTitle to title of n
        set noteTitle to do shell script "python -c \"import sys; print unicode(sys.argv[1], 'utf8').upper().encode('utf8')\" " & quoted form of noteTitle
        set title of n to noteTitle
    end repeat
end tell
```    

You can easily modify this code to use any simple kind of capitalization that you like. To change the capitalization, replace ".upper()" to something like ".title()". You can use any of the following:

  * `.upper()`
  * `.lower()`
  * `.title()`
  * `.capitalize()`
  * `.swapcase()`
