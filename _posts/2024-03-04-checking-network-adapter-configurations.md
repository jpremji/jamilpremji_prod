---
id: 161
title: 'Checking Network Adapter Configurations'
date: '2024-03-04T06:03:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=161'
permalink: /index.php/2024/03/04/checking-network-adapter-configurations/
burst_total_pageviews_count:
    - '3'
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

To get all network adapters and their DNS information using PowerShell, you can use the `Get-NetAdapter` cmdlet from the NetAdapter module to retrieve a list of network adapters, and the `Get-DnsClientServerAddress` cmdlet to retrieve the DNS server addresses for each adapter.

```
# Import the NetAdapter module

Import-Module NetAdapter

# Get a list of all network adapters

$Adapters = Get-NetAdapter

# Loop through the adapters

foreach ($Adapter in $Adapters) {

  # Get the DNS server addresses for the adapter

  $DnsServers = Get-DnsClientServerAddress -InterfaceAlias $Adapter.Name

  # Create a new object with the adapter and DNS server information

  $Object = [pscustomobject]@{

    Adapter = $Adapter.Name

    DnsServers = $DnsServers.ServerAddresses -join ','

  }

  # Write the object to the console

  $Object | Format-Table -AutoSize

}
```

But this doesn’t let you work with the data so we can change the $object and return it into a Variable like this

```
# Import the NetAdapter module

Import-Module NetAdapter

# Get a list of all network adapters

$Adapters = Get-NetAdapter

# Loop through the adapters

$AdapterInformation = foreach ($Adapter in $Adapters) {

  # Get the DNS server addresses for the adapter

  $DnsServers = Get-DnsClientServerAddress -InterfaceAlias $Adapter.Name

  # Create a new object with the adapter and DNS server information

  $Object = [pscustomobject]@jamilpremji

    Adapter = $Adapter.Name

    DnsServers = $DnsServers.ServerAddresses -join ','

  }

  # Write the object to the console

  $Object 

}
```

When returning something in PowerShell, it returns anything that is written to the pipeline.

Keep in mind that a function can return multiple values or objects by writing them to the pipeline or by using the `return` keyword. You can use the `Out-Default` cmdlet to write the output to the console or the `Out-File` cmdlet to write the output to a file. You can also use the `>` operator to redirect the output to a variable or to a file.