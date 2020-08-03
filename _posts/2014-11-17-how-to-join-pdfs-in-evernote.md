---
layout: post
title: How to join PDFs in Evernote
tags: evernote, applescript, published, share
notebook: Postach.io
---


<ins>UPDATED 2014-12-14 — Sometimes an Evernote note is produced with invalid characters.  The script below has been updated to strip out invalid characters.</ins>

Over on the Evernote forums, [jonteamere](https://discussion.evernote.com/user/221346-jonteamere/) said, “[it'd be nice to build, within EN, a single PDF document from individual docs.](https://discussion.evernote.com/topic/75343-feature-request-ability-to-combine-not-merge-individual-pdf-notes/)”

I've had an itch for the same feature.  It turns out that this is totally do-able in vanilla OS X.  The following script grabs the currently selected notes from Evernote (in their visible sort order) and their PDF attachments, then creates a new note with a single PDF.  It ignores non-PDF attachments.

```AppleScript
-- Join PDFs in multiple Evernote notes into a single PDF in a new note
-- Author: John Christopher Jones <john.christopher@alumni.virginia.edu>
-- Created: 2014-11-17
-- Updated: 2014-12-11 -- write utf8 and strip non-ascii characters when extracting hash values

-- inspired by
-- https://discussion.evernote.com/topic/75343-feature-request-ability-to-combine-not-merge-individual-pdf-notes/?locale=en
-- https://discussion.evernote.com/topic/24388-how-to-access-note-attachments-with-applescript/
-- https://applehelpwriter.com/2013/03/23/how-to-merge-pdf-files-in-os-x/

-- We'll join note titles together using this string
-- This isn't going to be a great title, but it'll be
-- a good reminder of what's in the new note.
set title_separator to " | "

-- Create a temporary folder for the exported Evernote attachments
-- Create an output filepath to write the joined pdf to
set temp_folder to do shell script "mktemp -d -t evernote_pdf"
set output_filepath to temp_folder & "/" & (do shell script "uuidgen") & ".pdf"

-- XSLT used to extract hash values from en-media tags
-- Crazy {} translation nonsense used to work around forum post scrubbers
set xslt to "{?xml version='1.0'?}
{xsl:stylesheet version='1.0' xmlns:xsl='https://www.w3.org/1999/XSL/Transform'
                xmlns:en='https://xml.evernote.com/pub/enml2.dtd'}
    {xsl:output method='text' omit-xml-declaration='yes' indent='no'/}
    {xsl:strip-space elements='*'/}
    {xsl:template match='en-media'}
        {xsl:value-of select='@hash'/}
        {xsl:text}&#xa;{/xsl:text}
    {/xsl:template}
    {xsl:template match='text()|@*'}{/xsl:template}
{/xsl:stylesheet}
"
set my text item delimiters to "{"
set xslt to text items of xslt
set my text item delimiters to "<"
set xslt to xslt as text
set my text item delimiters to "}"
set xslt to text items of xslt
set my text item delimiters to ">"
set xslt to xslt as text

-- Write XSLT to temporary location
set xslt_path to do shell script "mktemp -t evernote_enml"
tell application "Finder" to write xslt to xslt_path

-- Initialize some lists
set hash_values to {}
set pdf_list to {}
set title_list to {}

tell application "Evernote"
    -- Loop over every attachment in every note
    -- Note order follows the visible sort order in the OS X Desktop Client v5.7.2
    set noteList to selection
    repeat with n in noteList
        set the end of title_list to title of n

        -- Write the ENML to a temporary file and extract the en-media hash values
        set enml_text to (ENML content of n) as text
        set enml_path to do shell script "mktemp -t evernote_enml"
        tell application "Finder" to write enml_text to enml_path

        -- Extract the hash values from the ENML temporary file using the XSLT
        set hash_values to paragraphs of (do shell script "cat " & (quoted form of enml_path) & " | strings | xsltproc --novalid " & (quoted form of xslt_path) & " - ")
        -- Delete the temporary ENML file
        do shell script "rm " & (quoted form of enml_path)

        -- Export each attachment in the order that it appears in the note
        repeat with hash_value in hash_values
            -- Get the attachment that has this hash
            set a to item 1 of (attachments of n whose hash is hash_value)
            -- Write the attachment to the temporary folder
            set pdf_path to temp_folder & "/" & (do shell script "uuidgen") & ".pdf"
            write a to pdf_path as «class utf8»
            -- Save the filepath for later
            set the end of pdf_list to pdf_path
        end repeat
    end repeat

    -- We'll join PDF filepaths so that they're single-quoted and space-delimited
    set my text item delimiters to "' '"

    -- Join PDFs
    do shell script (quoted form of "/System/Library/Automator/Combine PDF Pages.action/Contents/Resources/join.py") & " --output " & (quoted form of output_filepath) & " " & ("'" & (pdf_list as text) & "'")

    -- Create a new note with a title built from the titles of the selected notes
    set my text item delimiters to title_separator
    set new_note to create note from file output_filepath title (title_list as text)

    -- Open the newly created note in a new window so the user doesn't have to wonder
    -- where the thing is and if it was actually created.
    open note window with new_note

    -- Delete all of the remaining temporary files
    do shell script "rm -r " & quoted form of temp_folder
    do shell script "rm " & quoted form of xslt_path
end tell
```

## Installation

I highly recommend [Keyboard Maestro](https://www.keyboardmaestro.com/) as an easy way to assign keyboard shortcuts to AppleScript scripts.

However, a free way to conveniently use this script is to [activate the script menu](https://vorpal.club/how-do-i-use-applescript#script-menu) via OS X's Script Editor, then save the script to the Evernote scripts folder.  You'll then be able to run the script from the script menu.

## Disclaimer

This script hasn't been rigorously tested, but it works for me.

## Credits

I needed to accomplish a few things with this script:

 1. pick out some Evernote notes,
 2. extract their attachments in a usable form,
 3. join the attachments, and finally
 4. create a new note and attach the joined document.

I learned from [philastokes's 2013-03-23 post](https://applehelpwriter.com/2013/03/23/how-to-merge-pdf-files-in-os-x/) that OS X comes with a bundled python script to join PDFs as part of the "Combine PDF Pages" Automator action.  Back in 2012 on the Evernote forums, [iNik demonstrated writing attachments from Evernote](https://discussion.evernote.com/topic/24388-how-to-access-note-attachments-with-applescript/).  The official [Evernote AppleScript Examples](https://dev.evernote.com/doc/articles/applescript.php) showed me the rest of the Evernote-specific stuff.
