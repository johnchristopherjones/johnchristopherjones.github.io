---
title: How do I use Javascript for Automation?
tags: ["idea"]
notebook: Postach.io
---

JavaScript for Automation is a little peculiar. You do **not** get the introspection you might expect. Collections of scripting bridge objects have to be called as methods to get their contents. i.e., method chaining. This is probably the most unintuitive thing you have to remember going into it. It’s actually pretty close to method chaining in jQuery.

  


For example, you might expect to be able to write “Mail.inbox.messages” to get mail messages in your inbox. Instead, you have to write “Mail.inbox().messages()”.

  


Unlike jQuery, you’re not dealing with the same object type (the wrapped set) after every method. Instead, you need to discover what members each object has from the Script Editor’s Dictionary.

  


In addition, you have access to Objective-C classes. You import these, but you start out with the foundation. These classes and anything you import does not polite the global namespace. Instead, imported members are added to the ‘$’ object. E.g., you can make a native Javascript string:

  


var myString = “a string”;

  


You can also make an NSString:

  


var myString = $.NSMutableString.alloc.initWithUTF8String(“a string”);

  


An example script for exporting Mail messages from Mail using Javascript for Automation.

```Javascript
var str, path;

var Mail = Application("Mail");

var subjects = Mail.inbox().messages().forEach(function (message, index, array) {
    str = $.NSMutableString.alloc.initWithUTF8String(message.messageSize() + "\n" + message.source());
    str.writeToFileAtomically('/Users/jcj/Desktop/messages/' + message.id() + '.emlx', true);
});

```
