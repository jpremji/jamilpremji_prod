---
id: 98
title: 'Easily Check How Long a Process has Been Running'
date: '2025-02-25T09:36:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=98'
permalink: /:year-:month-:day-:title
footnotes:
    - ''
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

To check how long a process has been running in PowerShell, you can use the `Get-Process` cmdlet and the `Uptime` property. The `Uptime` property returns the amount of time that the process has been running, in seconds.

```
# Get the current time

$currentTime = Get-Date

# Get the Firefox process

$firefoxProcess = Get-Process -Name firefox

# Get the start time of the Firefox process

$startTime = $firefoxProcess.StartTime

# Calculate the difference between the current time and the start time of the Firefox process

$timeRunning = $currentTime - $startTime

# Display the amount of time the Firefox process has been running

Write-Output "The Firefox process has been running for $timeRunning."
```

The code block above would return the following, if only 1 process of Firefox existed on this system.

> The Firefox process has been running for 18:36:12.1563877.

However, it would error out if multiple processes were running, because Get-Process returns an Object. There are multiple ways this can be fixed, here are two:

```
$firefoxProcess = Get-Process -Name firefox | Select-Object –First 1
```

This line could be changed to only return one result. The pipe to Select-Object, and providing the parameter, First, returns just the first item in the object. The Select-Object command has many other parameters you can read about, using: Get-Help Select-Object

 Another option is the following:

```
# Calculate the difference between the current time and the start time of the Firefox process

$timeRunning = $currentTime - $startTime[0]
```

Adding the \[0\] allows you to iterate through an object, in this case, selecting the first item in the object.

The code example below shows both options implemented in the script from earlier.

```
# Get the current time

$currentTime = Get-Date

# Get the Firefox process

$firefoxProcess = Get-Process -Name firefox | Select-Object -First 1

# Get the start time of the Firefox process

$startTime = $firefoxProcess.StartTime

# Calculate the difference between the current time and the start time of the Firefox process

$timeRunning = $currentTime - $startTime[0]

# Display the amount of time the Firefox process has been running

Write-Output "The Firefox process has been running for $timeRunning."
```

#### There is a mistake in the above code block

PowerShell contains a property called Count, it returns the number of elements in an object. If there is one item only, the Count property will return 0 because there are no elements in the object, only a single object.

For example, consider the following command:

```
$process = Get-Process -Name firefox
```

This command returns a single `System.Diagnostics.Process` object representing the Firefox process. If you try to access the `Count` property of the `$process` object, it will return `0` because there are no elements in the object, only a single object:

```
$process.Count

# Output: 0
```

To get the number of objects returned by a command, you can use the `Measure-Object` cmdlet, which allows you to count the number of objects in a collection. For example:

```
$processes = Get-Process

$count = $processes | Measure-Object | Select-Object -ExpandProperty Count
```

Or alternatively, we could have declared the $process variable before setting it.

```
$processes = @()

$processes = Get-Process

$Processes.Count # Outputs 1
```

To find a file with the “.csv” extension that was last modified a year ago on the D drive using PowerShell, you can modify the `-Filter` parameter of the `Get-ChildItem` cmdlet to search for files with the “.csv” extension.

```
$yearAgo = (Get-Date).AddYears(-1)

Get-ChildItem -Path "D:\" -Filter "*.csv" -Recurse | Where-Object {

  $_.LastWriteTime -lt $yearAgo

}
```

This script uses the `-Filter` parameter to search for files with the “.csv” extension on the D drive, using the `*` wildcard to match any characters before the extension. The output of the `Get-ChildItem` cmdlet is then piped to the `Where-Object` cmdlet, which filters the results based on the last write time of the file using the `LastWriteTime` property. It returns only the files that were last modified before the date a year ago.

To save the result to a variable, you can use the `$` symbol followed by a name for the variable. For example:

```
$yearAgo = (Get-Date).AddYears(-1)

$results = Get-ChildItem -Path "D:\" -Filter "*.csv" -Recurse | Where-Object {

  $_.LastWriteTime -lt $yearAgo

}
```

This script saves the result of the `Get-ChildItem` and `Where-Object` cmdlets to the `$results` variable.

To export the results to a CSV file, you can use the `Export-Csv` cmdlet. For example:

```
$yearAgo = (Get-Date).AddYears(-1)

$results = Get-ChildItem -Path "D:\" -Filter "*.csv" -Recurse | Where-Object {

  $_.LastWriteTime -lt $yearAgo

}

$results | Export-Csv -Path "C:\Temp\Results.csv" -NoTypeInformation
```