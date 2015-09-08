---
title: Setting up FileMaker to access ODBC sources
tags: ["filemaker", "odbc"]
notebook: Postach.io
---



http://www.milanm.com/?p=491
http://dev.mysql.com/downloads/connector/odbc/
https://my.bluehost.com/cgi/help/89

**Setting up ODBC to access FileMaker**

I've worked with MySQL, SQLite, FileMaker, and a few other databases. However, I'm a total ODBC newbie.

It turns out, I have a use case. I want to get data out of FileMaker, and I do _NOT_ want FileMaker in charge of when I can get the data. FileMaker has some pretty severe blocking behavior you can't get around. The way to control FileMaker without ODBC is to use AppleScript. Unfortunately, there are a lot of ways FileMaker can become unresponsive, or even respond out of order, to AppleScript Events. The fix is esentially to tell AppleScript to bash on the keyboard until FileMaker snaps out of it. I don't like that.

So, I need to get data out of FileMaker. I need to do it on my schedule. ODBC to the rescue... I hope?

## WTF is ODBC?

ODBC-land is full of alphabet soup. It's a special little corner of hell where programmers, sysadmins, and database admins, all come together and learn to hate each other.
