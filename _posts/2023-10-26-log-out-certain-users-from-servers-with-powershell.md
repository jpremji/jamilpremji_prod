---
id: 149
title: 'Log Out Certain Users from Servers with PowerShell'
date: '2023-10-26T09:36:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=149'
permalink: /:year-:month-:day-:title
burst_total_pageviews_count:
    - '35'
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

To query a Windows computer for all logged on users and log off a specific user using PowerShell, you can use the `quser` command to retrieve a list of logged on users and the `logoff` command to log off a specific user

```powershell
# Prompt for the user name

$UserName = Read-Host 'Enter the user name'

# Use the quser command to get a list of logged on users

$LoggedOnUsers = quser | Select-Object -Skip 1

# Loop through the logged on users

foreach ($LoggedOnUser in $LoggedOnUsers) {

  # Check if the user name matches the user we want to log off

  if ($LoggedOnUser.UserName -eq $UserName) {

    # Use the logoff command to log off the user

    logoff $LoggedOnUser.SessionName

  }

}
```

This script prompts the user for the user name of the user that should be logged off. It then uses the `quser` command to retrieve a list of logged on users and pipes the output to the `Select-Object` cmdlet to skip the first line of the output (which is a header line).

The script then loops through the logged on users and checks the user name of each one. If the user name matches the user that should be logged off, the script uses the `logoff` command to log off the user.

To execute the above code on a list of servers using PowerShell, you can use the `Invoke-Command` cmdlet to run the code on each server remotely.

```powershell
# Prompt for the user name

$UserName = Read-Host 'Enter the user name'

# Specify the list of servers

$Servers = 'Server1', 'Server2', 'Server3'

# Loop through the servers

foreach ($Server in $Servers) {

  # Try to log off the user from the server

  Try {

    # Use the Invoke-Command cmdlet to run the code on the server

    Invoke-Command -ComputerName $Server -ScriptBlock {

      # Use the quser command to get a list of logged on users

      $LoggedOnUsers = quser | Select-Object -Skip 1

      # Loop through the logged on users

      foreach ($LoggedOnUser in $LoggedOnUsers) {

        # Check if the user name matches the user we want to log off

        if ($LoggedOnUser.UserName -eq $args[0]) {

          # Use the logoff command to log off the user

          logoff ($LoggedOnUsers -split " ")[0]

        }

      }

    } -ArgumentList $UserName

  }

  Catch {

    # If the logoff command fails, write an error message to the console

    Write-Error "Failed to log off $UserName from $Server: $_"

  }

}
```

This script prompts the user for the user name of the user that should be logged off and specifies a list of servers. It then loops through the servers and uses the `Invoke-Command` cmdlet to run the code on each server remotely, passing the user name as an argument.

The code that is run on the servers uses the `quser` command to retrieve a list of logged on users and loops through the logged on users, checking the user name of each one. If the user name matches the user that should be logged off, the `logoff` command is used to log off the user.

If the `logoff` command fails on any server, an error message is written to the console.

Keep in mind that the `quser` and `logoff` commands are external commands, which means they are not natively available in PowerShell. They may not be available on all versions of Windows, and they may behave differently depending on the version of the operating system. You may need to modify the script to fit your specific needs or use alternative cmdlets or functions to achieve the same result.