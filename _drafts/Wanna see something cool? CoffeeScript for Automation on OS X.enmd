---
title: Wanna see something cool? CoffeeScript for Automation on OS X
tags: []
notebook: Postach.io
---

If you're running at least OS X 10.10 ("Yosemite"), then you can control OS X applications with CoffeeScript. OS X Yosemite introduced "JavaScript for Automation" as a scripting bridge language, letting you use JavaScript to control any application that has AppleScript support.

  


Since CoffeeScript is JavaScript, that means you can use CoffeeScript to control OS X apps. Just pipe coffee to osascript (`coffee -p | osascript -l JavaScript`).

  


The following CoffeeScript one-liner will create a new Evernote note in your default notebook for every message in your Inbox in Mail.app. It's written as a Bash script, since you need to pipe coffee to osascript to make it work.

  


coffee -sp << EOF | osascript -l JavaScript

Application('Evernote').createNote {title:m.subject(), withText:m.content()} for m in Application('Mail').inbox.messages()

EOF

  


It's pretty cool.
