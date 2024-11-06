---
id: 650
title: 'Create an Event Log Entry and Source'
date: '2024-05-20T09:26:00-04:00'
author: jamilpremji
layout: post
guid: 'https://www.jamilpremji.com:443/?p=650'
permalink: /:year-:month-:day-:title
burst_total_pageviews_count:
    - '11'
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---
![](assets/images/powershell.png)
This PowerShell script demonstrates how to write an event with a specific Event ID (3009) to the event logs. It includes a try-catch block to create the event source if it doesn’t already exist. The script utilizes the `Write-EventLog` cmdlet to write the event and provides flexibility to specify the event source, event message, event type, and event log. Running the script with administrative privileges is necessary to create event sources.

```powershell
$source = "MyScript"
$message = "An event with ID 3009 was logged."
$eventId = 3009
$eventType = "Information"
$eventLog = "Application"

try {
    if (![System.Diagnostics.EventLog]::SourceExists($source)) {
        [System.Diagnostics.EventLog]::CreateEventSource($source, $eventLog)
        Write-Host "Event source '$source' created."
    }
    Write-EventLog -LogName $eventLog -Source $source -EventId $eventId -EntryType $eventType -Message $message
} catch {
    Write-Host "Error creating event source or writing event: $_"
}
```

1. We start by defining the variables used in the script: 
    - `$source`: Represents the source of the event. It is typically the name of your script or application.
    - `$message`: Contains the message you want to include in the event.
    - `$eventId`: Specifies the specific Event ID you want to assign to the event.
    - `$eventType`: Determines the type of the event (e.g., Information, Warning, Error).
    - `$eventLog`: Specifies the name of the event log where you want to write the event (e.g., Application, Security, System).
2. The script sets up a try-catch block to handle any potential errors that may occur.
3. Inside the try block, the script checks if the event source exists using the `[System.Diagnostics.EventLog]::SourceExists($source)` method. If the source does not exist, it proceeds to create the event source using the `[System.Diagnostics.EventLog]::CreateEventSource($source, $eventLog)` method.
4. If the event source was created, the script displays a message in the console using the `Write-Host` cmdlet to indicate that the event source was successfully created.
5. Next, the `Write-EventLog` cmdlet is used to write the event to the specified event log (`$eventLog`) with the provided event source (`$source`), event ID (`$eventId`), event type (`$eventType`), and event message (`$message`).
6. If any errors occur during the event source creation or event writing, the catch block will catch the exception, and the error message will be displayed using `Write-Host` along with the error information (`$_`).
7. Lastly, it’s important to note that administrative privileges are required to create event sources, so the script should be run with administrative rights.