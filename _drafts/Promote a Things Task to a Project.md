---
title: Promote a Things Task to a Project
tags: published, things, applescript
notebook: Postach.io
---

I love to use Things, but it's got a few workflow problems. One of those problems is that it encourages you to capture, but assumes that whatever you capture is a “next actions” in GTD parlance. There's no easy way to promote a task to a project if that item needs to have sub-tasks.

It turns out that [Things has a nice AppleScript API](http://downloads.culturedcode.com/things/download/ThingsAppleScriptGuide.pdf), so I fixed it.
     
```AppleScript
tell application "Things"
    set my_todos to selected to dos
    repeat with selectedToDo in my_todos
        set project_name to name of selectedToDo
        set project_notes to notes of selectedToDo
        set project_tags to tag names of selectedToDo
        set project_duedate to due date of selectedToDo
        if project_duedate is not missing value then
            set newProjet to make new project with properties {name:project_name, notes:project_notes, tag names:project_tags, due date:project_duedate}
        else
            set newProjet to make new project with properties {name:project_name, notes:project_notes, tag names:project_tags}
        end if
        move selectedToDo to list "Trash"
        show newProjet
    end repeat
end tell
```

The above script will promote however many tasks you have selected into projects. It'll copy every field it can into the new project, move the original task into the trash, then “reveal” one of the newly created projects. Which project will be revealed is unfortunately fuzzy when there are multiple tasks selected. Things doesn't let you have multiple windows.

Seven years on, it'd be nice if the collaboration features were finished. Maybe we'll get them some time after Things 3?
