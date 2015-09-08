---
title: How to Copy Mail Message URL
notebook: Postach.io
tags:mail, applescript, published
---

It'd be great if you could link to Mail messages from other applications.  Turns out, you can!

So, the goal is to copy the a working link to the clipboard based on your current selection in Mail.  These links should work in virtually any application in either OS X and iOS.

If you use Keyboard Maestro, just download [my Keyboard Maestro macro](https://dl.dropboxusercontent.com/u/10516852/Copy%20Mail%20Message%20URL.kmmacros
).  (The default hotkey is CMD+CTRL+C)  Otherwise, you can use this AppleScript.

```AppleScript
tell application "Mail"
    set _sel to get selection
    set _links to {}
    repeat with _msg in _sel
        set _messageURL to "message://%3c" & _msg's message id & "%3e"
        set end of _links to _messageURL
    end repeat
    set AppleScript's text item delimiters to return
    set messageLinks to (_links as string)
    set the clipboard to messageLinks
end tell
```

I [posted about this on the Evernote forums](https://discussion.evernote.com/topic/18181-request-ability-to-link-to-emails-in-mac-mail/#entry90747) back in January.  Since then, I've backed my way into the above solution and found that I use it a lot.

## How does this work?

Every message has a unique ID, and both iOS and OS X implement a URL scheme for mail messages based on that unique ID.  That scheme is `message://`.  Now, this really should be be a [URN](http://en.wikipedia.org/wiki/Uniform_resource_name), not a [URI](http://en.wikipedia.org/wiki/Uniform_resource_locator#cite_note-10), but nobody likes URNs and nobody does them right.<sup>[<a href="http://en.wikipedia.org/wiki/Uniform_resource_identifier">Citation Needed</a>]</sup>

If you drag a Mail message into a text field, you'll get something that looks like this:

    message:%3C30190147.20141203032523.547e82a3c04bb6.21166770@mail131.wdc04.mandrillapp.com%3E

This is weird.  I don't recognize what this is supposed to be.  It's a URL encoded version of this:

    message:<30190147.20141203032523.547e82a3c04bb6.21166770@mail131.wdc04.mandrillapp.com>

It looks more like a URN than URL.  It also doesn't really work.  The angle brackets are probably a conceit that this is not a URI and shouldn't be resolved like one.  We can make a little tiny change to the first form to make it look more like a URI and it'll start magically working *EVERYWHERE*.

    message://%3C30190147.20141203032523.547e82a3c04bb6.21166770@mail131.wdc04.mandrillapp.com%3E

Adding that double slash does the trick.  I think this is what Apple intended, but didn't quite get.  A URN takes the form of `urn:scheme:nameid`.  In this case, it should be

    urn:message:30190147.20141203032523.547e82a3c04bb6.21166770@mail131.wdc04.mandrillapp.com

But, if you don't register your URN then you can't do this.  (Another reason people are cold to URNs.)  So, we do the URI scheme and let Mail handle the URI.

## Credits

I first read about this on [Daring Fireball](http://daringfireball.net/2007/12/message_urls_leopard_mail).  MacStories [covered most of this](http://www.macstories.net/tutorials/send-selected-mail-message-to-evernote-with-source-url/) back in 2012.