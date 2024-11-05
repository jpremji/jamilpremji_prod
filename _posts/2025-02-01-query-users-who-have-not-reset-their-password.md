---
id: 193
title: 'Query Users Who Have Not Reset Their Password'
date: '2025-02-01T22:03:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=193'
permalink: /:year-:month-:day-:title
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

To find all users in Active Directory (AD) who have not reset their own password, you can use the `Get-ADUser` cmdlet and filter the results based on the `PasswordLastSet` attribute.

The `PasswordLastSet` attribute represents the date and time that the user’s password was last set or reset. By default, when a user is created in AD, the `PasswordLastSet` attribute is set to “0” (zero), which means that the password has never been reset.

You can use the `Get-ADUser` cmdlet to retrieve all users whose `PasswordLastSet` attribute is set to “0”. Here’s an example of how you can do this using PowerShell:

```
Get-ADUser -Filter {PasswordLastSet -eq 0}
```

This command will retrieve all AD users whose `PasswordLastSet` attribute is set to “0”. You can use the `-Properties` parameter to specify which properties of the user objects you want to retrieve. For example, to retrieve the name and email address of the users, you can use the following command:

```
Get-ADUser -Filter {PasswordLastSet -eq 0} -Properties Name,EmailAddress
```

It’s important to note that the `PasswordLastSet` attribute may not always accurately reflect whether a user has reset their own password. For example, if an administrator has reset the user’s password, the `PasswordLastSet` attribute will be updated to reflect the date and time of the reset, even if the user did not reset their own password. Therefore, this method may not be completely reliable for determining whether a user has reset their own password.