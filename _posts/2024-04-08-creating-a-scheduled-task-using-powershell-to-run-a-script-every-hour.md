---
id: 654
title: 'Creating a Scheduled Task Using PowerShell to Run A Script Every Hour&#8221;'
date: '2024-04-08T09:32:00-04:00'
author: jamilpremji
layout: post
guid: 'https://www.jamilpremji.com:443/?p=654'
permalink: /:year-:month-:day-:title
burst_total_pageviews_count:
    - '80'
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

To create a scheduled task that runs a specific batch file every 1 hour using PowerShell, you can use the `New-ScheduledTask` cmdlet. Here’s an example command:

```
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument '-WindowStyle Hidden -File "C:\Scripts\autorun\start.ps1'
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Hours 1) -RepetitionDuration ([System.TimeSpan]::MaxValue)
$settings = New-ScheduledTaskSettingsSet
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "RunSrvGit" -Settings $settings

```

1. `$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument '-WindowStyle Hidden -File "C:\Scripts\autorun\start.ps1'`This line creates a new scheduled task action using the `New-ScheduledTaskAction` cmdlet. The action specifies that it will execute `powershell.exe`. The `-Argument` parameter specifies the arguments to be passed to the executable. In this case, it specifies `-WindowStyle Hidden -File "C:\Scripts\autorun\start.ps1'`, where `-WindowStyle Hidden` ensures that the PowerShell window is hidden, and `-File` specifies the path to the PowerShell script to be executed (`C:\Scripts\autorun\start.ps1`).
2. `$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Hours 1) -RepetitionDuration ([System.TimeSpan]::MaxValue)`This line creates a new scheduled task trigger using the `New-ScheduledTaskTrigger` cmdlet. The trigger is set to run once initially (`-Once`) at the current date and time (`-At (Get-Date)`). The `-RepetitionInterval` parameter specifies the interval between repetitions, which is set to 1 hour using `New-TimeSpan -Hours 1`. The `-RepetitionDuration` parameter is set to `[System.TimeSpan]::MaxValue`, indicating that the repetition should continue indefinitely.
3. `$settings = New-ScheduledTaskSettingsSet`This line creates a new scheduled task settings object using the `New-ScheduledTaskSettingsSet` cmdlet. This object provides additional settings for the scheduled task.
4. `Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "RunSrvGit" -Settings $settings`Finally, this line registers the scheduled task using the `Register-ScheduledTask` cmdlet. It specifies the task’s action (`$action`), trigger (`$trigger`), task name (`"RunSrvGit"`), and settings (`$settings`).