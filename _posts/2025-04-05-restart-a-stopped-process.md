---
id: 105
title: 'Restart a Stopped Process'
date: '2025-04-05T09:36:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=105'
permalink: '/?p=105'
footnotes:
    - ''
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

Suppose you have an application which crashes on its own and you need it to automatically start-up when this happens. PowerShell can help.

To monitor the Windows Audio service and start it if it is in a stopped state using PowerShell, you can use the following script:

> ```
> # Check the status of the Windows Audio service
> 
> $service = Get-Service -Name "AudioSrv"
> 
> # If the service is stopped, start it
> 
> if ($service.Status -eq "Stopped") {
> 
>   Start-Service -Name "AudioSrv"
> 
>   Write-Output "The Windows Audio service was stopped and has been started."
> 
> }
> ```

This script uses the `Get-Service` cmdlet to retrieve the status of the Windows Audio service, and checks if it is in a stopped state using the `Status` property. If the service is stopped, it uses the `Start-Service` cmdlet to start the service, and displays a message indicating that the service has been started.

You can run this script periodically using the `Task Scheduler` or a looping construct in your script to continuously monitor the status of the service.

In the script above, the Write-Output would not be logged anywhere, so you can write the item out to your EventLog.

> ```
> Write-EventLog -LogName "Application" -Source "ServiceMonitor" -EntryType Information -EventId 1 -Message "The Windows Audio service was stopped and has been started."
> ```

However, the command above will fail, because the ServiceMonitor source does not exist yet. We needed to create that first.

> ```
> # If the source does not exist, create it
> 
> if (-not $sourceExists) {
> 
>     New-EventLog -LogName "Application" -Source "ServiceMonitor"
> 
> }
> 
> Write-EventLog -LogName "Application" -Source "ServiceMonitor" -EntryType Information -EventId 1 -Message "The Windows Audio service was stopped and has been started."
> ```