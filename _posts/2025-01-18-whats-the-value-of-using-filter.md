---
id: 177
title: 'What’s the value of using Filter?'
date: '2025-01-18T09:36:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=177'
permalink: '/?p=177'
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - Uncategorized
tags:
    - PowerShell
---

Why is it better to use Get-ADUser -Filter {GivenName -eq “John”} in comparison to Get-AdUser -Filter \* | Where-Object

Using the `-Filter` parameter with the `Get-ADUser` cmdlet is generally more efficient than using the `Where-Object` cmdlet to filter the results of the `Get-ADUser` cmdlet.

When you use the `-Filter` parameter, the filtering is done by the Active Directory service, which is optimized for this task. On the other hand, when you use the `Where-Object` cmdlet, the filtering is done in the client side by the PowerShell process, which can be slower.

Additionally, using the `-Filter` parameter can reduce the amount of data that needs to be transferred over the network, as only the matching AD users are returned to the client. When you use the `Where-Object` cmdlet, all AD users are returned to the client and then filtered, which can use more network bandwidth.

Therefore, it is generally recommended to use the `-Filter` parameter whenever possible to optimize the performance and efficiency of your PowerShell scripts that query Active Directory.

In the example you provided, `Get-ADUser -Filter {GivenName -eq "John"}` will return only the AD users with a given name of “John”, while `Get-AdUser -Filter * | Where-Object` will return all AD users and then filter them based on the condition specified in the `Where-Object` cmdlet.