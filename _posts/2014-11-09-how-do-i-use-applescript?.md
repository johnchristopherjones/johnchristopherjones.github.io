---
layout: post
title: How do I use AppleScript?
tags: published, applescript
notebook: Postach.io
---
I've sometimes been asked how to use the [AppleScript](https://developer.apple.com/library/mac/documentation/AppleScript/Conceptual/AppleScriptX/AppleScriptX.html) scripts I throw around.  There are just shy of a bazillion ways to invoke some AppleScript.  Here, I'll attempt to collect some of the common ways to run a script.

I'll start with the native ways to run AppleScript in OS X without any additional apps, then throw in a few third-party apps I like.

## Native ways to run AppleScript

Let's start with the ways built into OS X.  These are features built into OS X that don't require any third-party add-ons.

### The [Apple]Script Editor

In OS X Yosemite, AppleScript Editor was renamed to [Script Editor](https://developer.apple.com/library/mac/documentation/AppleScript/Conceptual/AppleScriptX/Concepts/work_with_as.html).  It's the same app, but it gets some long-overdue serious attention.

To run any AppleScript, you can:
 1. open Script Editor;
 2. create a new document (Menu bar » File » New);
 3. paste the script in; then
 4. hit the "run" button (with the "play" icon).

This app is usually where you write and test any AppleScript that you create yourself, unless you live and breathe [XCode](https://developer.apple.com/xcode/).  Even if you're writing AppleScript that will ultimately be embedded into another application (e.g., FileMaker), this is usually a good place to test, tweak, and perfect your script.

However, you probably want to have your scripts at your command in a specific application, rather than CMD+Tabbing over the Script Editor, opening a script, and hitting run.

#### Export as an Application

In Script Editor, you can export a script as an application (.app).  Once that's done, you can just run the app to run your script.  The app will launch in the Dock and then quit once the script finishes running.  You can keep the app in the dock, run it with Spotlight, double-click it in a folder, or whatever you like.

To export a script as an application:

 1. go to the menu bar and choose File » Export…;
 2. in the "File Format:" drop-down menu, choose "Application"; then
 3. give it a name and save it somewhere.

To run the application you just created, just double-click it from wherever you saved it.  You can of course move it somewhere else if you like.

### <a name="script-menu"/>The Script System Menu (disabled by default)

Script Editor lets you enable a Script [status menu](https://support.apple.com/en-us/HT3737) item.  This is hidden in the General tab of Script Editor's preferences (Menu bar » Script Editor » Preferences).  When this status menu item is enabled, you'll have quick access to any scripts that you've saved in specific folders.  When you save a script in the correct folder, it automatically shows up in this menu.

You can reveal these special locations by clicking on the Script Menu icon, expanding the "Open Scripts Folder" sub-menu, and choosing one of the options, which will be:

 - Open {Current Application} Folder
 - Open User Scripts Folder
 - Open Computer Scripts Folder

Each of these folders turns out to be `~/Library/Scripts/Applications/{Current Application}/`, `~/Library/Scripts/`, or `/Library/Scripts`.  For example, for Pages this folder would be `~/Library/Scripts/Applications/Pages/`.  The folder for your specific application might not exist yet; if not, choosing the "Open {Current Application Folder}" item will automatically create the folder, but it's just a normal folder that you can yourself.

The script menu is "good enough" for most people.  It's built in, point and click, and free.

### Automator

You can use Automator and Keyboard Shortcuts in System Preferences to create an application-specific keyboard shortcut to run an AppleScript.  Automator is a tool Apple created to try to bring some of the power of AppleScript to more regular users.  It's not bad, but we're here to talk AppleScript.

To create an application-specific keyboard shortcut for an AppleScript:

 1. open Automator;
 2. create a new Automator workflow (Menu bar » File » New);
 3. when asked to "Choose a type for your document", choose "Service";
 4. in the right column at the top, choose "no input" in the first drop-down and the specific application you want this script to run in (you can also choose "any application");
 4. search the actions in the left sidebar for "Run AppleScript" and double-click;
 5. in the Run AppleScript action that appears in the right column, paste your script;
 6. save your document in Automator;
 7. call it something descriptive (in this example, "Peanut Brittle");
 8. (optional) quit Automator;
 9. open System Preferences (Apple menu » System Preference…);
 10. open Keyboard;
 11. click the Shortcuts tab;
 12. click "App Shortcuts" in the left column;
 13. click "+" at the bottom of the right column;
 14. choose the application you used in Automator from the dropdown;
 15. type the name of your service (e.g., "Peanut Brittle");
 16. click into the "Keyboard shortcut" box and press the keyboard shortcut you want to use (I like to use CMD+CTRL for most of my shortcuts);
 17. go to your application and try it out.

While not hard, this is a pretty scattered process.  For that reason, I prefer to use a third-party app called Keyboard Maestro whenever I want a keyboard shortcut for an AppleScript.

<!--
## What is Automator?
Starting in Mac OS X 10.4 (Tiger), Apple created a new application called Automator to try to bring the power of AppleScript to people who weren't comfortable with Script Editor.  For many use cases they succeeded, but it was a rocky start.  Automator is installed with OS X.

The Automator application creates documents called "workflows".  Each workflow is composed of a list of "actions". One action might prompt you for a folder.  Another action might rename files.  Link them together and you've got a workflow that prompts you for a folder and renames all the files in the folder.

Automator also lets you make special kinds of workflows called "Services".  Services will show up under the "Services" sub-menu in the application's menu.  These Services are (optionally) application-specific and (optionally) context-specific.  For example, you can make an Automator Service that only works on Folders in Finder.  If you don't have a folder selected in Finder, the service doesn't show up.
-->

### Command-line

You can run any AppleScript from Terminal or anywhere else you can run shell scripts.  Just run the command `osascript` followed by the path to the script (escape spaces and whatnot in the path or wrap the path in quotes).  The script can be stored in a `.scpt` file, a `.scptd` folder ("script bundle"), or a `.applescript` text file.

You can also use the hash-bang trick to run AppleScript like any shell script.  Just make sure the very first line of your script is either:

```Bash
#!/usr/bin/osascript
```

or

```Bash
#!/usr/bin/env osascript
```

If you set the file permissions to executable (`chmod +x pathtoscript`) you can run the script just like any other shell script.  You can even run it from `launchd` or `cron`.

### Application-Specific Options

Certain applications in OS X explicitly let you invoke AppleScript.  Not many of the apps that come with OS X do this, but there are a few.

#### Mail.app

Mail lets you automatically run AppleScript whenever a message fits one of your Mail rules.  Mail rules are set under the Rules tab of Mail's preferences (Menu bar » Mail » Preferences).  From this tab, Add or Edit a rule, then you can choose "Perform AppleScript" as one of the actions.

This can be pretty powerful, since Mail has good scripting support.

## Third-party ways to run AppleScript

The native ways can be a little out-of-the-way or scattered, so various third-party apps have sprung up that either let you manage your scripts centrally or give you easier ways to invoke them.  Here are a few of my favorites.

### Keyboard Maestro

[Keyboard Maestro](https://www.keyboardmaestro.com) can be thought of as a phenomenally easier-to-use variant on the built-in `Automator.app` method.  Keyboard Maestro lets you define macros that can run when various events happen on your system.  These events can include:

 - typing keys or key combos;
 - switching, opening, or closing an app;
 - mounting a volume; and/or
 - connecting/disconnecting from a network.

 In response, Keyboard Maestro runs a "macro".  That macro can include any number of hundreds of actions, including conditional tests, loops, and pauses.  One of those actions can be "Execute AppleScript".  The AppleScript can be pasted literally into Keyboard Maestro, or Keyboard Maestro can run a script that's saved as a file (including via iCloud or iCloud Drive).

 This is how I run almost all of my AppleScripts, since the app lets you set the AppleScript and the keyboard shortcut in the same place, rather than going through the Automator dance of creating a Service then going to `System Preferences » Keyboard` to set a keyboard shortcut for the menu item for that service.

### Alfred

 Alfred is something I don't personally use.  However, it's like a friendlier version of Automator married with Keyboard Maestro.  It looks a lot more like Automator, and Alfred [documents how to run scripts](https://support.alfredapp.com/tutorials:hotkeys) well enough that I won't repeat them.
