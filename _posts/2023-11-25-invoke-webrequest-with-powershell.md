---
id: 205
title: 'Invoke-WebRequest with PowerShell'
date: '2023-11-25T21:36:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=205'
permalink: /:year-:month-:day-:title
burst_total_pageviews_count:
    - '154'
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

`Invoke-WebRequest` is a PowerShell cmdlet that retrieves data from a web page or web service. The data returned from the web request can be in various formats, including JSON.

`ConvertFrom-Json` is a PowerShell cmdlet that converts a JSON-formatted string to a PowerShell object. This allows you to work with the data as native PowerShell objects, rather than as a JSON string.

Using `Invoke-WebRequest` and `ConvertFrom-Json` together allows you to easily retrieve JSON data from a web service and convert it into a usable format in your PowerShell script.

For example, you could use `Invoke-WebRequest` to retrieve a JSON response from a web service, and then use `ConvertFrom-Json` to convert the response into a PowerShell object. This allows you to access and manipulate the data within the object, rather than having to parse the JSON string manually.

Here is a script that uses `Invoke-WebRequest` to get your IP information from :

```powershell
# Get IP information from ipinfo.io
$response = Invoke-WebRequest "https://ipinfo.io/geo"

# Convert the response to JSON

$json = ConvertFrom-Json $response.Content

# Display the IP address

$json.ip
```

This script is using the Invoke-WebRequest cmdlet to send an HTTP request to the URL ““. This URL returns information about the location and IP address of the client making the request.

The script then uses the ConvertFrom-Json cmdlet to convert the response content, which is in JSON format, into a PowerShell object.

Finally, the script accesses the “ip” property of the resulting object and displays it on the screen. This will show the IP address of the client making the request.

To export the JSON response from the ipinfo API to a CSV file, you can use the `Export-Csv` cmdlet. Here’s an example of how you can do this:

```powershell
# Create an object from the JSON response
$object = [pscustomobject]$json

# Export the object to a CSV file

$object | Export-Csv -Path ".\export.csv" -NoTypeInformation
```

You can also customize the properties that are exported to the CSV file by using the `Select-Object` cmdlet to select only the properties that you want to include in the CSV file. For example:

```powershell
$object | Select-Object ip, city, region, country | Export-Csv -Path ".csv" -NoTypeInformation
```