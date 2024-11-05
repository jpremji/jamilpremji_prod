---
id: 101
title: 'How to Automate Deleting Older Files from a Directory'
date: '2025-03-15T21:36:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=101'
permalink: /:year-:month-:day-:title
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

To delete files in the `C:\Temp` directory that are older than 180 days using PowerShell, you can use the `Get-ChildItem` cmdlet with the `-Recurse` and `-Force` parameters, and the `Where-Object` and `Remove-Item` cmdlets.

```
# Calculate the date 180 days ago

$cutoffDate = (Get-Date).AddDays(-180)

# Get the list of files in C:\Temp that are older than 180 days

$oldFiles = Get-ChildItem -Path "C:\Temp" -Recurse -Force | Where-Object {

  $_.LastWriteTime -lt $cutoffDate

}

# Delete the old files

$oldFiles | Remove-Item -WhatIf
```

This script uses the `Get-ChildItem` cmdlet to get the list of files in the `C:\Temp` directory, including hidden and system files. The `-Recurse` parameter specifies that the search should be recursive, so that it searches all subdirectories as well. The `-Force` parameter specifies that hidden and system files should be included in the results.

The output of the `Get-ChildItem` cmdlet is piped to the `Where-Object` cmdlet, which filters the results based on the last write time of the file using the `LastWriteTime` property. It returns only the files that were last modified before the date 180 days ago.

**The command above, will delete all folders as well. See further below for the explanation of –WhatIf**

In case we want to preserve the directories we can make the following change:

```
# Calculate the date 180 days ago

$cutoffDate = (Get-Date).AddDays(-180)

# Get the list of files in C:\Temp that are older than 180 days and are not directories

$oldFiles = Get-ChildItem -Path "C:\Temp" -Recurse -Force | Where-Object {

  (-not $_.PSIsContainer) -and ($_.LastWriteTime -lt $cutoffDate)

}

# Delete the old files

$oldFiles | Remove-Item -WhatIf
```

#### What is –WhatIf in the Code Above?

Many functions in PowerShell, have the –WhatIf parameter built into them. When –WhatIf is supplied to these functions, they simulate the action they are going to take, and return the result, however, the action is not taken.

$WhatIfPreference = $true can be used at the start of the script to pass this parameter value to all calls when performing a dry-run, to reduce the number of changes to each line of code. Here is an example:

```
# Enable the WhatIf parameter

$WhatIfPreference = $true

# Test the effect of a cmdlet with the WhatIf parameter enabled

Get-ChildItem -Path C:\temp -WhatIf

# Disable the WhatIf parameter

$WhatIfPreference = $false

# Execute the cmdlet normally

Get-ChildItem -Path C:\temp
```