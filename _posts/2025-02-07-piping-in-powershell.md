---
id: 84
title: 'Piping in PowerShell'
date: '2025-02-07T09:36:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=84'
permalink: /:year-:month-:day-:title
footnotes:
    - ''
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

In PowerShell, piping is a way to pass the output of one command as the input to another command. This allows you to chain multiple commands together and perform complex operations in a single line of code.

The piping operator in PowerShell is `|`, which is also known as the “pipe” symbol. To use piping, you can place the `|` symbol between two commands, like this:

```
command1 | command2
```

This will execute `command1` and pass its output to `command2` as input.

```powershell
Get-Process | Where-Object { $_.WorkingSet -gt 2000000 } | Sort-Object -Property WorkingSet | Format-Table -Property Name, WorkingSet
```

This example retrieves a list of processes running on the computer, filters out processes with a working set less than 2 MB, sorts the remaining processes by working set size, and then formats the output as a table with the process name and working set size.

Piping is a powerful feature in PowerShell that allows you to perform complex tasks with just a few lines of code. It is an essential part of working with PowerShell and is widely used in scripts and interactive sessions.

![](assets/images/2022-12-piping.png)