---
layout: post
title: How to keep logged tallies in Evernote
tags: evernote, applescript, published, share
notebook: Postach.io
---

You do something a several times per day and you either want to record the last time you did it and how many times you did it.  Sometimes you want to make a note about what you did.  You're not really concerned with duration, so a time tracking app is a bad fit.

For example, somebody asked me if there was an easy way to do this to help hold themselves accountable for their flashcard study sessions:

> I'm in medical school and spend a good bit of time sitting in front of my computer memorizing random facts (Anki--which I understand is Python-based). I'll go for 10 or 25 minute blocks of time, all the while keeping a 'tally' of those blocks--usually on a post-it note. ← this way I hold myself accountable.
>
> Why not record those tallies in EN or TextEdit? Would this be hard to do with Applescript?

So, you have a few problems.

  1. You need a place to store your log entries.
  2. You need an easy way to make a new entry.
  3. You need to reduce repetitive things like entering timestamps.
  4. You want an automatic count.

We can accomplish this by appending entries to an Evernote note just fine, but the automatable stuff should be automated.  It'd be nice to just fire a script from any application and have a dialog pop up to ask us if we want to add a comment.  Add your comment or not then hit enter.  Automatically, your log is  appended with your comment (if any) and the current timestamp.  The header for today is also updated with the current tally for the day.

So, here's a script to do just that.  It adds log entries to a note named "My Log Note" (change it in the second line of the script).  If the note doesn't exist, it'll be created.  Add it to a macro in [Keyboard Maestro](http://www.keyboardmaestro.com/main/) or the [Script System Menu](http://vorpal.club/how-do-i-use-applescript#script-menu) and you're good to go.

```AppleScript
-- The tally note should have this title (change it to whatever you like)
set tallies_note_name to "My Log Note"

-- If you don't want comments on your notes, just replace this first tell block with:
--      set tally_annotation to ""
--
-- Tell the current application to show the dialog so that we can see it wherever we are
tell current application
    display dialog "A tally will be added to an Evernote note named " & (quoted form of tallies_note_name) & ".  You can add a comment:" with title "Create a tally" default answer ""
    -- Script will cancel at this point if the users chooses cancel
    set tally_annotation to (text returned of result) as string
end tell

-- To learn how to manipulate Evernote via AppleScript, check out Evernote's examples:
-- https://dev.evernote.com/doc/articles/applescript.php

tell application "Evernote"
    -- Calculate current date and timestamp strings
    set current_timestamp to first paragraph of (do shell script "date +'%F %T'")
    set current_date to first paragraph of (do shell script "date +'%F, %a'")
    set current_datestamp to first paragraph of (do shell script "date +'%F'")

    -- Denote the start of today this way (you'll need to tweak the < h1 > tags later in the script if you change this)
    set new_today_header to "<" & "h1>" & current_date & " (total: 0)<" & "/h1>"

    -- Find the tally note
    -- Evernote has a rich search syntax:
    -- https://dev.evernote.com/doc/articles/search_grammar.php#Search_Terms
    set matches to find notes "intitle:\"" & tallies_note_name & "\""

    -- If the tally note doesn't exist yet, create it.  Otherwise, fetch it from the matches.
    if length of matches is 0 then
        set tally_note to create note title tallies_note_name with html new_today_header
    else
        set tally_note to item 1 of matches
    end if

    -- Get the HTML representation for the note content
    set tally_html to HTML content of tally_note

    -- Calculate with the start of today looks like in the note
    set today_split to "<" & "h1>" & current_date

    -- If today hasn't been added to the note, add it.
    if today_split is not in tally_html then
        tell tally_note to append html new_today_header
        -- Re-grab the HTML representation for the note content
        set tally_html to HTML content of tally_note
    end if

    -- Let's calculate the total number of tallies for today
    set my text item delimiters to current_datestamp
    set today_count to (length of text items of tally_html) - 1

    -- Let's rewrite the count for today
    set my text item delimiters to today_split
    set head_html to text item 1 of tally_html
    set tail_html to text item 2 of tally_html
    set my text item delimiters to "<" & "/h1>"
    set tail_tail_html to text item 2 of tail_html
    set HTML content of tally_note to head_html & today_split & " (total: " & today_count & ")<" & "/h1>" & tail_tail_html

    -- Append a timestamp for right now
    tell tally_note to append html ("<" & "div><" & "span style=\"font-family: courier new\">" & current_timestamp & "<" & "/span> " & tally_annotation & "<" & "/div>")

    -- Tell the current application to show the dialog so that we can see it wherever we are
    tell current application to display dialog "The note was successfully appended." buttons {"View Note", "Cancel"} cancel button "Cancel" default button "Cancel"
    -- Script will cancel at this point if the user chooses cancel
    set new_window to open note window with tally_note
end tell
```
