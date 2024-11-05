---
id: 668
title: 'Sending an e-Mail using Python and Office365 SMTP'
date: '2024-05-06T14:14:00-04:00'
author: jamilpremji
layout: post
guid: 'https://www.jamilpremji.com:443/?p=668'
permalink: /index.php/2024/05/06/sending-an-e-mail-using-python-and-office365-smtp/
burst_total_pageviews_count:
    - '16'
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

```
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email server information
smtp_server = 'smtp.example.com'
smtp_port = 587

# Email content
subject = 'Test Email Send'
message = 'This is a test email.'

# Sender and recipient
from_address = 'sender@example.com'
to_address = 'recipient@example.com'

# Email credentials
username = 'your_username@domain.com'
password = 'your_password'

# Create the email
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Create the SMTP connection
server = smtplib.SMTP(smtp_server, smtp_port)

# Start the connection
server.starttls()

# Login with credentials
server.login(username, password)

# Send the email
server.sendmail(from_address, to_address, msg.as_string())

# Quit the server
server.quit()

print('Email sent successfully.')

```

## Parameters to change

username – **This is your e-mail addresssubject**

from\_address – **This has to be the same as the username or and SMTP alias of the mailbox**

message –

to\_address –

password –

This helps you avoid the reliance on SMTP port 25.

## Encrypted Password

To encrypt your password on Windows, you can use the [securestring library](https://github.com/er28-0652/securestring)

First create a password using PowerShell

```
"your password" | ConvertTo-SecureString -AsPlainText -Force | ConvertFrom-SecureString | Out-File "c:\passwordfile.txt"
```

```
from securestring import securestring
original_file = open("c://passwordfile.txt", "r")
lines = original_file.readlines()
password = securestring.decrypt(lines[0])
```