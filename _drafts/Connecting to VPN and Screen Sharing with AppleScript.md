---
title: Connecting to VPN and Screen Sharing with AppleScript
tags: 
  - published
  - applescript
notebook: Postach.io
published: true
---


I need to VPN into a network where the VPN is provided by OS X 10.8 Server. Unfortunately, the VPN tends to fail the first couple of times you try to connect if nobody has tried to connect recently. This makes the whole dance of connecting to the VPN and opening up Screen Sharing to my workstation a little tedious.

I set up the following script so that I can just fire-and-go. It'll try to reconnect a couple of times before automatically opening Screen Sharing to my workstation. The names and numbers have been changed to protect the innocent.
    
```AppleScript
tell application "System Events"
    tell network preferences
        -- discover if the VPN is connected
        set myConnection to location "Automatic"
        set myService to service "VPN (vpnserver.local)" of myConnection
        set isConnected to false

        -- if the VPN isn't connected, keep trying until we succeed
        repeat while not isConnected
            set isConnected to connected of current configuration of myService
            if isConnected is false then
                connect current configuration of myService
                delay 5
            end if
        end repeat
    end tell
end tell

-- if the VPN is connected, open screen sharing
tell application "Screen Sharing"
    GetURL "vnc://10.0.0.8"
end tell
```
