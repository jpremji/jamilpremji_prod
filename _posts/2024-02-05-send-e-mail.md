---
id: 197
title: 'Send E-Mail'
date: '2024-02-05T18:03:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=197'
permalink: /:year-:month-:day-:title
burst_total_pageviews_count:
    - '1'
categories:
    - PowerShell
tags:
    - PowerShell
---

To send an e-mail notification using PowerShell, you can use the `Send-MailMessage` cmdlet. This cmdlet allows you to specify the sender, recipient, subject, and body of the e-mail, as well as any additional parameters such as the SMTP server to use for sending the e-mail.

Here’s an example of how you could use the `Send-MailMessage` cmdlet to send an e-mail notification:

```powershell
$smtpServer = "smtp.example.com"
$to = "recipient@example.com"

$from = "sender@example.com"

$subject = "Notification from PowerShell"

$body = "This is a notification message sent from PowerShell."

Send-MailMessage -SmtpServer $smtpServer -To $to -From $from -Subject $subject -Body $body
```

You can also use the `-Attachments` parameter to include attachments in the e-mail, or the `-Credential` parameter to specify a username and password to use for authenticating with the SMTP server.

The Send-MailMessage cmdlet is a legacy cmdlet that was introduced in PowerShell v1. It is used to send an email message using the Simple Mail Transfer Protocol (SMTP). It is obsolete and is not recommended for use in new scripts.

Instead, you can use the .NET class `System.Net.Mail.SmtpClient` to send email messages. This class provides more options and better performance compared to the Send-MailMessage cmdlet.