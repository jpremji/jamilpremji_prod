---
id: 167
title: 'Get Local Administrators on Servers'
date: '2024-02-26T06:03:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=167'
permalink: /:year-:month-:day-:title
burst_total_pageviews_count:
    - '9'
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

To get a list of local administrators on a server using PowerShell, you can use the `Get-LocalGroupMember` cmdlet from the Security module to retrieve the members of the local “Administrators” group.

```powershell
# Get the members of the local "Administrators" group

$Admins = Get-LocalGroupMember -Group "Administrators"

# Loop through the members

foreach ($Admin in $Admins) {

  # Write the member name to the console

  Write-Output $Admin.Name

}
```

This script uses the `Get-LocalGroupMember` cmdlet to retrieve the members of the local “Administrators” group.

The script then loops through the members and writes the name of each member to the console using the `Write-Output` cmdlet.

You can modify the script to fit your specific needs, such as by filtering the list of members based on certain criteria or by writing the output to a file instead of the console. You can also use the `-ComputerName` parameter of the `Get-LocalGroupMember` cmdlet to specify a different computer, if necessary.

Keep in mind that the `Get-LocalGroupMember` cmdlet requires local administrator privileges to run, and it may not be available on all versions of Windows. You may need to use alternative cmdlets or functions to achieve the same result on other operating systems or configurations.

```powershell
# Run the net localgroup command and store the output in a variable

$Output = net localgroup "Administrators"

# Split the output into lines

$Lines = $Output -split "`n"

$logging = $false 

# Loop through the lines

foreach ($Line in $Lines) {

  # Check if the line starts with "*"

  if ($Line -match "^---*") {

    # Split the line into words

    # Write the second word to the console (which should be the member name)

    $logging = $true

  }

  elseif ($line -match "The command completed") {

      $logging = $false

  }

  if ($logging -eq $true -and $line -notmatch "^---*") {

      Write-Output $Line

  }

}

```

This script is written in PowerShell and it does the following:

It runs the net localgroup command and stores the output in a variable called $Output. This command lists the members of the local group “Administrators”.

It splits the output into lines and stores the resulting array of lines in a variable called $Lines.

It initializes a variable called $logging and sets it to $false. This variable will be used to keep track of whether the script should log the member names to the console or not.

It starts a loop that iterates through each line in the $Lines array.

For each line, it checks if the line starts with “—” (using the -match operator). If it does, it sets the $logging variable to $true to indicate that the script should start logging the member names to the console.

If the line does not start with “—“, the script checks if the $logging variable is $true. If it is, it checks if the line is not equal to “—” (using the -notmatch operator). If the line is not equal to “—“, the script writes the line to the console using the Write-Output cmdlet.

If the line matches “The command completed”, the script sets the $logging variable to $false to stop logging member names to the console.

In summary, this script runs the net localgroup command, parses the output, and writes the names of the members of the “Administrators” group to the console.