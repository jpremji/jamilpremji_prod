---
id: 201
title: ConvertFrom-Json
date: '2024-03-08T18:03:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=201'
permalink: /index.php/2024/03/08/convertfrom-json/
burst_total_pageviews_count:
    - '7'
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

The `ConvertFrom-Json` cmdlet in PowerShell is used to convert a string in JavaScript Object Notation (JSON) format into an object that is recognizable by PowerShell. This cmdlet allows you to work with JSON data directly in PowerShell, rather than having to parse the data manually. It is commonly used when working with REST APIs or other web-based services that return data in JSON format.

First we need an object. Run the following code snippet to generate a file. It will create names.json in your shell directory.

```
# Create an array of first names
$firstNames = @(
    'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Gary', 'Hannah', 'Igor', 'Jill',
    'Kate', 'Laura', 'Mike', 'Nina', 'Olivia', 'Peter', 'Quincy', 'Rachel', 'Sam', 'Tina',
    'Ursula', 'Victor', 'Wendy', 'Xander', 'Yvette', 'Zach'
)

# Create an array of last names
$lastNames = @(
    'Adams', 'Baker', 'Chase', 'Davies', 'Evans', 'Foster', 'Garcia', 'Harrison', 'Ingram', 'Johnson',
    'Kendall', 'Lopez', 'Mendoza', 'Nguyen', 'Owens', 'Parker', 'Quinn', 'Roberts', 'Simmons', 'Taylor',
    'Upton', 'Vargas', 'Wright', 'Xavier', 'Young', 'Zimmerman'
)

# Initialize an empty array to store the JSON objects
$jsonArray = @()

# Generate 30 random names and create a JSON object for each one
for ($i = 1; $i -le 30; $i++) {
    # Get a random first and last name
    $firstName = $firstNames[$(Get-Random -Minimum 0 -Maximum $firstNames.Count)]
    $lastName = $lastNames[$(Get-Random -Minimum 0 -Maximum $lastNames.Count)]

    # Create a JSON object with an ID and the first and last name
    $jsonObject = @{
        'id' = $i
        'firstName' = $firstName
        'lastName' = $lastName
    }
    $jsonArray += $jsonObject
}

# Convert the array of JSON objects to a single JSON string and write it to a file
$jsonString = $jsonArray | ConvertTo-Json
$jsonString | Out-File 'names.json'

```

This code first creates two arrays of first and last names. Then it creates an empty array to hold the JSON objects. It uses a for loop to create 30 JSON objects, each with a unique id, a random first name, and a random last name. The JSON objects are added to the `$jsonArray` array. The `$jsonArray` array is then converted to a single JSON object using the `ConvertTo-Json` cmdlet. Finally, the JSON object is exported to a text file using the `Out-File` cmdlet.

To import a JSON file and use the `ConvertFrom-Json` cmdlet to convert it to a PowerShell object, you can use the following code:

```
# Import the JSON file
$json = Get-Content -Path .\names.json -Raw

# Convert the JSON file to a PowerShell object
$names = ConvertFrom-Json -InputObject $json

# Access the objects in the array
$names[0]
$names[1]

# Access the properties of the objects
$names[0].id
$names[0].firstName
$names[0].lastName

```

This will import the `names.json` file, convert it to a PowerShell object, and allow you to access the objects in the array and the properties of those objects.

For example, if `names.json` contains the following JSON:

```
[
  {
    "id": 1,
    "firstName": "John",
    "lastName": "Doe"
  },
  {
    "id": 2,
    "firstName": "Jane",
    "lastName": "Doe"
  }
]

```

Then running the above code would allow you to access the objects in the `$names` array and their properties, like this:

```
PS C:\> $names[0]
id          : 1
firstName   : John
lastName    : Doe

PS C:\> $names[1]
id          : 2
firstName   : Jane
lastName    : Doe

PS C:\> $names[0].id
1
PS C:\> $names[0].firstName
John

PS C:\> $names[0].lastName
Doe


```