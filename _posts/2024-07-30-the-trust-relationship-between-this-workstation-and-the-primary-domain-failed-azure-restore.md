---
id: 846
title: 'The trust relationship between this workstation and the primary domain failed &#8211; Azure Restore'
date: '2024-07-30T21:29:20-04:00'
author: jamilpremji
layout: post
guid: 'https://www.jamilpremji.com:443/?p=846'
permalink: /:year-:month-:day-:title
burst_total_pageviews_count:
    - '4'
categories:
    - azure
    - PowerShell
---

When restoring an Azure server you may run into the following issue, “The trust relationship between this workstation and the primary domain failed,” where you see an error when logging in as Local Admin.

![](assets/images/2024-07-trust.jpg)If you try with an user/domain privileged account, you see “the user name or password is incorrect. Try again.”

![](assets/images/2024-07-autologon-the-username-or-password-is-invalid-1024x683.jpg)In this case you need a powershell script, which has to be run from the “Run Command” option on your Azure VM portal. You can’t use INvoke-Command as your credentials will fail because the logon fails as well. Same issue when using Bastion.

In the run command, add the following

```
$username = "domain\username"
$password = ConvertTo-SecureString "PasswordHere" -AsPlainText -Force
$credential = NewObject System.Management.Automation.PSCredential($username,$password)
Reset-ComputerMachinePassword -Credential $credential
```

Update: This is for when you have a server that doesn’t let you logon as local admin. After failing to reset the password using the Run Command option.