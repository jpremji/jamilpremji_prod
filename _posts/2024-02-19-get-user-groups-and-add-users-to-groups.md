---
id: 181
title: 'Get User Groups and Add Users to Groups'
date: '2024-02-19T06:03:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=181'
permalink: /:year-:month-:day-:title
burst_total_pageviews_count:
    - '6'
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

To find the Active Directory (AD) groups that a user is a member of, you can use the `Get-ADPrincipalGroupMembership` cmdlet in PowerShell.

```powershell
# Import the ActiveDirectory module  
Import-Module ActiveDirectory  

# Get the AD user object  
$User = Get-ADUser -Identity “John Smith”  

# Get the AD groups that the user is a member of  
Get-ADPrincipalGroupMembership -Identity $User

```

The `Get-ADPrincipalGroupMembership` cmdlet returns an array of `ADGroup` objects representing the AD groups that the user is a member of. You can use the `Name` property of each `ADGroup` object to get the name of the group.

You can also use the `-Recursive` parameter to get the nested membership of the user, which includes the groups that the user is a member of, as well as the groups that those groups are a member of, and so on.

You can find more information about the `Get-ADPrincipalGroupMembership` cmdlet in the PowerShell documentation.