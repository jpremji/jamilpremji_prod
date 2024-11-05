---
id: 185
title: 'Query Active Directory Computers'
date: '2024-03-25T22:00:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=185'
permalink: /index.php/2024/03/25/query-active-directory-computers/
burst_total_pageviews_count:
    - '4'
categories:
    - PowerShell
tags:
    - PowerShell
---

To query all Active Directory (AD) computers in a specific organizational unit (OU) using PowerShell, you can use the `Get-ADComputer` cmdlet and specify the `-SearchBase` parameter to specify the OU.

```
Get-ADComputer -Filter * -SearchBase "OU=Computers,DC=contoso,DC=com"
```

This command will retrieve all AD computers in the “Computers” OU within the “contoso.com” domain.

You can also use the `-Properties` parameter to specify which properties of the computer objects you want to retrieve. For example, to retrieve the name and operating system of the computers, you can use the following command:

```
Get-ADComputer -Filter * -SearchBase "OU=Computers,DC=contoso,DC=com" -Properties Name,OperatingSystem
```

You can also use the `-SearchScope` parameter to specify the search scope. By default, the search scope is set to “Subtree”, which means that the cmdlet will search the specified OU and all its child OUs. If you want to search only the specified OU and not its child OUs, you can set the search scope to “OneLevel”.

```
Get-ADComputer -Filter * -SearchBase "OU=Computers,DC=contoso,DC=com" -SearchScope OneLevel
```