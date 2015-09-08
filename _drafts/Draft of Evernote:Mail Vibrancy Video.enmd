---
title: Draft of Evernote/Mail Vibrancy Video
notebook: Postach.io
tags:evernote, os x, vibrancy, draft
---

Clips
=====

## Introduction

* Evernote recently released 6.0.3.
* It's a remake to make Evernote blend in with Yosemite.
* I have a few suggestions to improve Evernote 6, which I'll go over.

I'm going to preface with an explanation of the major UI trick of Yosemite, which is the translucency effect they call "Vibrancy".  I think this is necessary because UI design is a language for communicating with the user, and Evernote 6.0.3 needs some help with its grammar.

## What is Vibrancy?

* What is window chrome vs content?
* Burn and blend, not transparency
    - Opaque or vibrant; nothing between
* Content first
    - Window chrome is getting out of the way (blending content through)
    - Content is opaque, never blended
* Note, contrast is never subtracted from content itself

### Purpose of Vibrancy

* Give user content prominence over window decorations
* Add contrast between content elements where chrome spacing has been added
    - User content pops through dressing like side bars
* Add contrast between content and chrome
    - User content pops through dressing like toolbars

Vibrancy is a highlight of OS X, but the default view of Mail is opaque and 100% user content.  That user content blends through the toolbar, letting user content have the run of 100% of the window geometry.

## Evernote Suggestions

When filing a bug report it's best to describe the expected behavior and contrast that with the observed behavior.  To demonstrate the expected behavior I'll be using Mail, which has similar UI needs to Evernote.

### Drawing/Vibrancy issues

* Notebook selection is invisible
* Note list is translucent
* Note list selection is translucent
* Multiple levels of translucency being used
    - Mail uses exactly two: opaque, vibrant
* Border between notelist and note is hard to see
    - Mail uses edge-to-edge opacity for single message.
    - Mail uses vibrant margins for multiple messages
    - Evernote could use opaque edge-to-edge for single message
    - Evernote should provide "conversation view" on multiple selection like Mail; current "hand of cards" effect is less useful.  Would correspond well with functionality of Presentation Mode.
* Fonts are not system fonts, don't respect accessiblity options

### Respect the layers (z-fighting)

* Part of note panel is blended; scrolling causes content to dive under
    - impression is that note is somehow diving under the app that's below Evernote
* Note list vanishes under column and toolbar
* Note list column header doesn't let content blend through
* Toolbar doesn't let note list blend through
* Note list is translucent
* Note list selection is transparent

### Follow the OS X selection guidelines

* Note list selection uses border instead of inverted colors
    - communicates input textbox (show Safari)
    - communicates not-yet-chosen selection (accessiblity)
* Where else do we see the border?  CMD*SHIFT*I!
    - border indicates focus, not selection.  Text selection is inverted
* Where else?
    - User interface elements not yet selected (Mail Preferences)
        * miscommunicating that selection HASN'T HAPPENED
* Inverted colors especially important with the language of Vibrancy
    - Selection is inverted, strong, dominant color.
    - Selection blends through chrome, putting user action ahead of application chrome.
    - Helps user orient; gives sense of space and speed beyond scroll pane

### Miscellaneous

* Tab order in Show Info is incorrect
* Move Note (CMD*CTRL*M) doesn't work from note title field (works from note body)
* App Preferences doesn't respect keyboard navigation
* Window menu needs a way to bring back app, or Evernote should close
* Dismissing App Preferences causes drawing errors
* Top bar in note list is redudant with sidebar

    Could get rid of a lot of UI struggles by doing what Mail does.
    Evernote would be a good match for the Safari/Maps style of a search menubar.

        - Not a document window
        - Search is primary
        - Would provide a great place to put share/present buttons
        - Evernote's top bar is overweight

    - If you want a top bar, try a variant of what Mail does
        * "Notebooks" and "Tags" dropdowns, "Shortcuts" across the top

* Default stylesheet in OS X is inferior to the iOS styelsheet.
    Poor vertical spacing between paragraphs.


---


This is a little crash course on the UI effects of the "Vibrancy" effect in OS X Yosemite.

As of December 1st, 2014, Evernote has released Evernote 6.0.1 and has been having a little bit of trouble getting the hang of Yosemite and Yosemite's Vibrancy visual effect in particular.  The forums have been kinda noisy, so this is my attempt to nail a couple of concrete points down.

Yosemite has been a bit of an acid test for apps that implement non-native or custom widgets.  Apps that have followed the Apple guidelines and used system defaults have flourished, while apps that rely on crossplatform hackery have had issues.

There's a great contrast between Mail and Evernote.  Mail can be considered a gold standard for how Vibrancy in supposed to work in Yosemite.  Mail and Evernote have extremely similar UI needs, so they're a great pair of apps to compare and constrast.

Here's a key point.  Vibrancy does something very specific.  It's supposed to make your personal content pop and make you aware of your personal content that's just beyond the boundaries of the scroll pane.  If you just throw blending effects at the wall you're not going to hit the mark at all.

You can see this in the way that Mail uses Vibrancy.  Mail uses opaque backgrounds for your content.  It uses vibrant backgrounds for your ancillary content, like folders.  [The folder column is disabled by default, but you only ever glance at it if you enable it.]  Vibrancy also blends your content through the toolbar and column headers, adding to your awareness of what's beyond the scroll pane.

Another key point is that Vibrancy is used to ADD contrast to your content.  It NEVER substracts contrast from your content.  That sidebar is not content.  Vibrancy blends margins, helping you distinguish between padding and content.


Focused selection is indicated by an inverted color scheme
    - This puts user action foremost
    - The inverted colors pop through the vibrancy column header and toolbar, again pulling your content through the chrome.
    - Adds awareness of selection scrolling past the top of the window
    - Sidebar also uses inverted colors for selection

Scroll column in Evernote has three different levels of transparency; no opacity at all.

Evernote selection:
    - Sidebar, WTF is selected?
    - All content is blended
    - Mulitple levels of blending going on; Mail uses just two: on and off
    - Scroll column is not blending thorugh the colun header or toolbar

Content panel
    - Mail uses two different content panels: solo and conversation
    - Solo pops to the full pane size, opaque, putting content first
    - Conversation adds a lot of contrast to help demark threads
    - Evernote always blends as though in conversation view
    - Vibrancy in Evernote is very muted, doesn't add any contrast, but it doesn't add any information (demarkation) in the first place so it's just noise
    - Evernote fonts don't respect system fonts; mish-mash of fonts

So I can't know what Evernote has done behind the scenes here—what's going on in the Evernote app.  They've clearly attempted to make a Yosemite *theme*/Vibrant *theme* but it's not achieving the objectives of Vibrancy; it's running counter to them.  It's not accomplishing the mission of Yosemite and Vibrancy, which to really being the content foremost, and that's something Evernote really should be able to get behind.

There are a couple of things Evernote could do to improve things.  The first thing is to follow Mail's lead and make content opaque.  Content should never have a blended background.  Second, reduce visual complexity.  There should only ever be two backgrounds in the app: Opaque and vibrant.  Any compromise between vibrant and opaque is an error.  Third, Evernote should use the system convention of solid backgrounds for selections.  This applies to both the note list and the sidebar.  Fourth, try getting rid of the note margins in the content panel.  They add noise without information—Mail gets this one right.

-----

Yosemite has been a bit of an acid test for apps that implement non-native or custom widgets.  Apps that have followed the Apple guidelines have and used system defaults have made the transition smoothly.  Vibrancy in particular has been hard for really customized apps to get right.
 
There's a great contrast between Mail and Evernote.  Mail can be considered a gold standard for how Vibrancy is supposed to work in Yosemite.  Mail and Evernote have extremely similar UI needs, so there're a great pair of apps to compare and contrast.
 
Here's a key point.  Vibrancy does something very specific.  It's supposed to make your personal content pop and make you aware of your personal content just beyond the boundaries of the scroll pane.  If you just throw blending effects at the wall you're not going to hit the mark at all.
 
You can see this in the way that Mail uses Vibrancy.  Mail uses opaque backgrounds for your content.  It uses Vibrant backgrounds for your ancillary content, like sidebars.  Sidebars aren't content, so they get the vibrancy background to distinguish them from content.  This increases the contrast between the ancillary matter and your own content.  Vibrancy also blends your opaquely-backgrounded content through the toolbar and column headers, adding to you awareness of what's just beyond the scroll pane.  Your content is not only opaque, but it burns through the toolbar to get to you.
 
Another key point is that Vibrancy is used to ADD contrast to your content.  It NEVER subtracts contrast from your content.  That sidebar in Mail is not content.  Vibrancy blends margins, helping you distinguish between padding and content.
 
Mail uses the system standard of solid backgrounds for selection, both in the message list and in the sidebar.  Blue is the system default, but if you choose another color in General Settings, then Mail and every other app uses that color.  This puts the user's action foremost.  This solid background has additional weight with Vibrancy, because the solid background nearly glows through the toolbar when it scrolls past the scroll pane.  This shows the user's action is being respected and emphasized, to the expense of the window chrome.  Evernote, by contrast, uses a faded blue border reminiscent of  button focus in Mavericks.  It's hard to spot and breaks system conventions—the blue border means the indicated element is not yet selected, yet Evernote uses it to indicate ​current selection.  Personally, it causes me to act uncertainly and I'm never quite sure which note is selected.  In addition, there's no indication of what notebook is selected in the Evernote sidebar.  Mail, again, uses a solid background in the vibrant sidebar to indicate selection, though it's a vibrant background because it's a vibrant panel.
 
Another thing to note is that Mail uses exactly TWO backgrounds: vibrant and opaque.  Content is opaque, and ancillary or marginal space is vibrant.  Any compromise between those two choices is an error.  Evernote uses no less than three levels of opacity.  The sidebar is the weakest opacity (which does not appear to be the native Vibrancy effect, which is a burn effect not the blur-and-blend effect Evernote uses).  The column view itself uses a slightly heavier opacity, and the selected note in the note list uses an even heavier opacity.  The overall effect is to be blurry.
 
The content panel is another point of contrast.  Mail uses exactly two kinds of content panels.  The first is the single-message panel.  The single message panel is opaque, edge-to-edge with the message list.  Note that the mailbox sidebar is hidden by default in Mail, which means the default view in Mail is 100% opaque.  The second kind of content panel is the conversation view.  In this view, the messages are still 100% opaque but the margins between and around messages take on a vibrant background.  This adds contrast, helping you spot the dividing space between the messages in the conversation view.  The hard boundary line between the message list and the message panel is always obvious.
 
Evernote, by contrast, uses a blended background in the content panel.  This blended background isn't adding information like it does in Mail.  There's only ever one note in the content panel in Evernote, so it should be edge-to-edge flush opaque.  It might make sense to go vibrant if you have Related Notes (or "Context") visible.  In the Evernote content panel, there's a rounded border around the note body and that blended background is reminiscent of the linen background that we killed back in Mavericks with most of the skeuomorphism. It just adds noise, and makes the boundary between the note list and the note hard to see.
 
A particularly glaring fault in Evernote's use of the language of Vibrancy in Evernote is that when you scroll down the note, the note vanishes behind the blended background of the toolbar/infopanel/buttonbar thingy at the top of the note.  That is, not only is the note body not popping out through the toolbar, it's vanishing behind the background.  In an FPS game, that'd be a drawing order bug, which is particularly disorienting.  
 
There are a couple of things Evernote could do to improve things.  First, Evernote should follow Mail's lead and make content opaque.  Content should never have a blended background.  Second, reduce visual complexity.  There should only ever be two backgrounds in the app: opaque and vibrant.  Any compromise between vibrant and opaque is an error.  Third, Evernote should use the system convention of solid background for selections.  This applies to both the note and the sidebar.  Fourth, try getting rid of the margins in the content panel.  They add noise without information—Mail gets this one right.  Fifth, please just standardize on the system standard single font face.  I don't mean just matching the font, but using the system definition.  OS X has taking big strides to resolution independence, and Yosemite lets users really tweak their fonts for accessibility, including bumping the font size and font weight up.  Evernote uses smaller fonts when people are trying to use bigger fonts.  If Evernote uses the system font definitions then people can bump the font size up in System Preferences and get the results they expect.

