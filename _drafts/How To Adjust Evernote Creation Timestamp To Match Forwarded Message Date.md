---
title: How To Adjust Evernote Creation Timestamp To Match Forwarded Message Date
notebook: Postach.io
tags:evernote, applescript, published, share
---

Evernote has a feature that lets you forward emails to file notes away in specific notebooks with specific tags.  While a great feature, Evernote dates the notes by the date they were forwarded, not the date of the original message.  I wanted my Evernote notes to have the creation date of the original imessage.

On the Evernote forums, [mwaddell requested this same feature](https://discussion.evernote.com/topic/19396-feature-request-backdating-notes-via-email/?hl=%2Bforwarded+%2Bmessage+%2Bdate) back in 2011.

“Why?” you might ask.  I use this feature a lot.  In the simplest case, I forward invoices and receipts.  I do this because I also scan paper receipts and invoices, so they all wind up in the same searchable place.  Sometimes I pull something out of my email archives that I want to hold onto.  Ultimately, I want it all to fall into my timeline in the order that it happened.

I tried a couple of different approaches to this.  I had to fall back onto Python for a lot of it, because AppleScript's date manipulation and string processing facilities are somewhat horrific.

```AppleScript
-- Set the creation date of the current Evernote note to the date displayed in a forwarded message header
-- Author: John Christopher Jones <john.christopher@alumni.virginia.edu>
-- Created: 2014-11-29

tell application "Evernote"
    -- Loop over every attachment in every note
    -- Note order follows the visible sort order in the OS X Desktop Client v5.7.2
    set noteList to selection
    repeat with n in noteList
        -- Remove "Fwd: " from note tile
        try
            set my text item delimiters to "Fwd: "
            set title of n to text item 2 of ((title of n) as text)
        end try
        
        -- Save HTML to temproary file
        set html_text to (HTML content of n) as text
        set temp_filepath to (do shell script "mktemp -t evernote_html")
        tell application "Finder" to write html_text to temp_filepath
        
        -- Extract date from HTML
        set python_script to quoted form of "import sys, re, dateutil.parser; datestring = re.sub(r'<[^>]*>', '', re.search(r'Date: *((?:(?!<br|</div).)+)', sys.stdin.read()).group(1)); print dateutil.parser.parse(datestring).strftime('%x %I:%M:%S %p')"
        try
            set new_date to do shell script ("cat " & quoted form of temp_filepath) & " | python -c " & python_script
            do shell script "rm " & quoted form of temp_filepath
        end try
        
        -- Update creation date
        set creation date of n to date new_date
    end repeat
end tell
```

There are a couple of tricks to this.  First, I don't like the "Fwd:" prefix polluting my note titles, so I strip that off immediately.  Second, I write the note's HTML to a temporary file to make it easier to handle in Python.  

The regex uses a negative lookahead to look for the break after the date label no matter how the email header was formatted in Evernote, then strips out any HTML tags poluting the match.

There's a lot of magic in the rest of the Python section of this script.  First of all, Python has a `dateutil.parser` module that is quite amazing at processing date strings.  The date string in an email can be formatted approximately a bajillion ways, so `dateutil.parser` is a perfect tool to interpret the date string that was extracted from the HTML.  Now, I've got a date object ready to be output into a format AppleScript understands!  Right?

Like I said, [date processing in AppleScript is hard](http://macscripter.net/viewtopic.php?id=24737).  Part of this is because *there is no **sane** locale-invariant way to create dates*.  I work around this slightly by taking advantage of the fact that Python has some locale-specific awareness of date formats.  I use strfprint's `%x` formatter to output a locale-specific date, then I output the time in a way that AppleScript requires, because AppleScript couldn't handle strfprint's `%X` format, nor `%c`.  This is the magical part that might not work for you.

Lastly, I convert the magically correct date string to a date object and set the creation date of the note to that value.

There's another way to get a locale-invariante date in AppleScript, but it's really obnoxious.  Essentially, you have to:

```AppleScript
-- Create a new date object
set new_date to current date
-- get a delimited list of date parts whose order and delimiter you know
set my text item delimiters to return
set date_parts to do shell script "python -c 'import datetime; print chr(10).join(str(x) for x in datetime.datetime.now().timetuple())'"
-- then change each element of the new_date object as though it were a record
set year of new_date to item 1 of text items of date_parts
set month of new_date to item 2 of text items of date_parts
set day of new_date to item 3 of text items of date_parts
set hours of new_date to item 4 of text items of date_parts
-- kill me already...
set minutes of new_date to item 5 of text items of date_parts
set seconds of new_date to item 6 of text items of date_parts
```

All of that is JUST initializing the date object—something that ought to be as simple as `date "2014-11-29 13:00:01"`.  The equivalent to that entire block in my Python script was `.parse(datestring)`.  This is one of those reasons people don't like AppleScript—sometimes most painful way of doing something is the most reliable way of doing that thing.