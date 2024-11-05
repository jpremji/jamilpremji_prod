---
id: 173
title: 'Query Active Directory Users'
date: '2025-01-09T21:36:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=173'
permalink: '/?p=173'
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

To query Active Directory (AD) users, you can use the `Get-ADUser` cmdlet in PowerShell.

```
# Import the ActiveDirectory module

Import-Module ActiveDirectory

# Query AD users

Get-ADUser -Filter *

# Query AD users with specific properties

Get-ADUser -Filter * -Properties SamAccountName, GivenName, Surname

# Query AD users with specific filter

Get-ADUser -Filter {GivenName -eq "John"}

# Query AD users in a specific OU

Get-ADUser -Filter * -SearchBase "OU=Users,DC=contoso,DC=com"
```

The `Get-ADUser` cmdlet has many options and parameters that you can use to filter and customize the query. For example, you can use the `-Filter` parameter to specify a filter for the query, the `-Properties` parameter to specify which properties to include in the output, and the `-SearchBase` parameter to specify the organizational unit (OU) to search.