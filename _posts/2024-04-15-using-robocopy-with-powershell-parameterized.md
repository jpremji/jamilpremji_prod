---
id: 658
title: Using RoboCopy with PowerShell – Parameterized
date: 2024-04-15T09:36:00-04:00
author: jamilpremji
layout: post
guid: https://www.jamilpremji.com:443/?p=658
permalink: /:year-:month-:day-:title
burst_total_pageviews_count:
  - "13"
categories:
  - PowerShell
tags:
  - PowerShell
---

The code sets the source path, destination path, and log file path using variables. It creates an array variable (`$robocopyParams`) that holds the parameters for the `robocopy` command, including the source, destination, and log file paths. Finally, it executes the `robocopy` command using the parameters from the `$robocopyParams` array.

```powershell
$sourcePath = "C:\Path\to\source"
$destinationPath = "C:\Path\to\destination"
$logPath = "C:\Path\to\log\file.log"

$robocopyParams = @(
    $sourcePath,
    $destinationPath,
    "/E",
    "/COPYALL",
    "/LOG:$logPath"
)

Robocopy @robocopyParams

```

1. `$sourcePath = "C:\Path\to\source"`: Sets the source path of the files or directories you want to copy.
2. `$destinationPath = "C:\Path\to\destination"`: Sets the destination path where the files or directories will be copied to.
3. `$logPath = "C:\Path\to\log\file.log"`: Specifies the path and filename for the log file that will capture the output of the `robocopy` command.
4. `$robocopyParams = @(...)`: Creates an array variable named `$robocopyParams` that holds the parameters for the `robocopy` command.
5. `$sourcePath`, `$destinationPath`: The source and destination paths are added as individual elements to the `$robocopyParams` array.
6. `"/E", "/COPYALL"`: The `/E` switch copies all subdirectories, including empty ones. The `/COPYALL` switch copies all file information including timestamps, attributes, and NTFS security permissions. These switches are added as separate elements to the `$robocopyParams` array.
7. `"/LOG:$logPath"`: The `/LOG` switch specifies the log file path. The `$logPath` variable is added as part of the element in the `$robocopyParams` array.
8. `Robocopy @robocopyParams`: Executes the `robocopy` command using the splatting technique, passing the individual elements of the `$robocopyParams` array as parameters to the `robocopy` command.