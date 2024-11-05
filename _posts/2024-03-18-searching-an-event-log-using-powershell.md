---
id: 133
title: 'Searching an Event Log Using PowerShell'
date: '2024-03-18T01:33:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=133'
permalink: /index.php/2024/03/18/searching-an-event-log-using-powershell/
burst_total_pageviews_count:
    - '6'
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

Suppose you want to search your event logs for the last time someone logged onto a server. PowerShell makes it easy. Or suppose you want to know the last time a certain event occurred.

To search the event log for events with a specific event ID using PowerShell, you can use the `Get-EventLog` cmdlet to retrieve the events and then use the `Where-Object` cmdlet to filter the events based on the event ID.

For example, the following command retrieves all events from the application event log and filters them by the “4624” event ID:

> ```
> $Events = Get-EventLog -LogName "Application" | Where-Object { $_.EventId -eq 4624 }
> ```

This command retrieves all events from the application event log and then uses the `Where-Object` cmdlet to filter the events based on the value of the `InstanceId` property. The `Where-Object` cmdlet compares the value of the `InstanceId` property to the value “4624” using the `-eq` operator, which stands for “equal to.”

You can specify any event ID that you want to search for by replacing the value “4624” with the desired event ID.

You can also use the `Get-EventLog` cmdlet to search for events in other logs, such as the system event log or the security event log. Simply specify the name of the log that you want to search in the `-LogName` parameter. For example:

You can then print out $Events

> ```
> $Events = Get-EventLog -LogName "Security" | Where-Object { $_.EventId -eq 4624 }
> ```

![](assets/images/2022-12-EventsList.png)The `Get-EventLog` cmdlet returns events as objects, with each object representing a single event. The properties of the event objects, such as `EventId`, `TimeGenerated`, and `Message`, can be accessed using dot notation, as in `$Event.EventId` or `$Event.TimeGenerated`.

However, when you use the `Format-Table` cmdlet to display the events, only the properties that are included in the table view will be shown. By default, the `Format-Table` cmdlet includes only a limited set of properties in the table view.

To include the `EventId` property in the table view, you can use the `-Property` parameter of the `Format-Table` cmdlet to specify the properties that you want to include. For example:

> ```
> $Events | Format-Table -Property EventId, TimeGenerated, Message
> ```

This command displays the `EventId`, `TimeGenerated`, `Message`, `Source`, and `UserName` properties of the events in a table.

Keep in mind that the properties that are available on the event objects depend on the log and the type of event. Not all properties will be available for all events.

If you want to look through the object in PowerShell, you can also use a for loop, to filter through the results.

```
$Events | ForEach-Object {
    Write-Host $_.EventId
}
```

The `ForEach-Object` cmdlet will iterate through each event in the `$Events` collection, and the code inside the loop will be executed for each event. The `$_` variable represents the current item being processed by the loop. In this case, the `$_.EventId` property of the current event is accessed and printed to the console using the `Write-Host` cmdlet.