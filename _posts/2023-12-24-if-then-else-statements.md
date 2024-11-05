---
id: 54
title: 'If / Then / Else Statements'
date: '2023-12-24T06:03:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=54'
permalink: /:year-:month-:day-:title
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

In PowerShell, an `if` statement allows you to execute a block of code based on the evaluation of a conditional expression. An `elseif` clause allows you to specify additional conditions that are checked only if the previous `if` or `elseif` condition was `false`. An `else` clause specifies a block of code that is executed if all the previous conditions were `false`.

```
$x = 10

if ($x -gt 15) {

    # This block of code is executed if $x is greater than 15

    Write-Host "x is greater than 15"

} elseif ($x -lt 5) {

    # This block of code is executed if $x is less than 5

    Write-Host "x is less than 5"

} else {

    # This block of code is executed if none of the previous conditions are true

    Write-Host "x is between 5 and 15"

}
```