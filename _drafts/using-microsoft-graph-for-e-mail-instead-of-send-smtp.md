---
layout: post
title: Using Microsoft Graph for E-Mail instead of Send-SMTP
permalink: /:year-:month-:day-:title
date: 2026-01-01
---

[Microsoft does not recommend](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/send-mailmessage?view=powershell-7.4&viewFallbackFrom=powershell-7.3) using the `Send-SMTP` cmdlet in PowerShell anymore for sending emails. This cmdlet was part of the older Exchange Management Shell (EMS) and was deprecated in favor of using other methods, such as the Graph API or the `Send-MailMessage` cmdlet, which is still supported for basic email sending tasks.

In order to use Graph, there are multiple methods

1. Microsoft Graph Application
2. Token Authentication

In order to use the Microsoft Graph Application, you need to to first create an application.

1. Create a new application in Microsoft Entra ID