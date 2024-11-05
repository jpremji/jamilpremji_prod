---
id: 114
title: 'Create a Scheduled Task Automatically'
date: '2025-02-16T21:36:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=114'
permalink: '/?p=114'
footnotes:
    - ''
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

To create a scheduled task using the Register-ScheduledTask cmdlet, you can use the following script.

```
# Create a trigger that runs the task daily at 9:00 AM

$Trigger = New-ScheduledTaskTrigger -Daily -At 9:00AM

# Create an action that runs a script named "myscript.ps1"

$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File C:\scripts\myscript.ps1"

# Set the task settings to allow multiple instances of the task to run concurrently

$Settings = New-ScheduledTaskSettingsSet -MultipleInstances

# Set the principal for the task to run as the system account

$Principal = New-ScheduledTaskPrincipal -UserId "NT AUTHORITY\SYSTEM" -LogonType ServiceAccount

# Create the scheduled task

Register-ScheduledTask -Trigger $Trigger -Action $Action -Settings $Settings -Principal $Principal -TaskName "DailyScriptTask"
```

This script will create a new scheduled task named “DailyScriptTask” that runs the script “myscript.ps1” every day at 9:00 AM, using the system account as the user to run the task. The task will be set to allow multiple instances to run concurrently.

You can customize the trigger, action, and other settings as needed. For example, you can use the `-Once` parameter to specify a one-time trigger, or the `-WeeksInterval` parameter to specify a recurring trigger that runs every X weeks. You can also specify the `-StartBoundary` and `-EndBoundary` parameters to set the start and end times for the task.

For more information on the `Register-ScheduledTask` cmdlet and its parameters, you can refer to the Microsoft documentation:



![](assets/images/2022-12-ScheduledTask.png)### That script won’t work though!

If you are having issues with a PowerShell script not running correctly when scheduled as a task, one potential issue could be that the script is not running in the correct environment. By default, scheduled tasks do not run with an interactive user profile, which can cause issues if the script relies on certain user-specific settings or resources.

To resolve this issue, you can specify the -NoProfile parameter when running the script in the scheduled task action. This parameter tells PowerShell to skip loading the user profile when executing the script, and can help ensure that the script runs correctly in the non-interactive environment of a scheduled task.

Here’s an example of how you can modify the scheduled task action to include the -NoProfile parameter:

```
$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -File C:\scripts\myscript.ps1"
```

This will tell PowerShell to skip loading the user profile when executing the script, which can help resolve issues with the script not running correctly as a scheduled task.

It’s also a good idea to include the full path to the PowerShell executable in the -Execute parameter, as shown above, to ensure that the correct version of PowerShell is being used to run the script.

If you are still having issues with the script not running correctly as a scheduled task, there may be other issues at play. Some common issues to check for include:

Permissions issues, such as the task not having sufficient privileges to access certain resources

Dependencies or external resources that are not available when the task runs

Syntax errors or other issues with the script itself

By troubleshooting and addressing these potential issues, you should be able to get the script running correctly as a scheduled task.