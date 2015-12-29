---
layout: post
title: How to write and run AppleScript in FileMaker without pain
tags: idea
notebook: Postach.io
---

 - Do not use Calculated AppleScript
 - Read and write to special purpose Global fields
 - Write top-level AppleScript errors to special purpose Global fields
 - Use calculations to manage FileMaker IO to the global fields

    ```FileMaker
    Set Field [@Global::AppleScriptOutput; Let ( $appleScriptOutput = @Global::AppleScriptOutput ; "" )
    ```
