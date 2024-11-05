---
id: 109
title: 'How to Search a File on Your Computer'
date: '2025-03-06T09:36:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=109'
permalink: /:year-:month-:day-:title
footnotes:
    - ''
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

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