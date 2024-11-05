---
id: 119
title: 'Sorting a CSV File Using PowerShell'
date: '2025-03-25T09:36:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=119'
permalink: '/?p=119'
footnotes:
    - ''
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

#### PowerShell and CSV Files

PowerShell provides several cmdlets that can be used to work with CSV (Comma Separated Value) files. Some examples of what you can do with PowerShell and CSV files include:

- Import data from a CSV file into a PowerShell script using the Import-Csv cmdlet. This cmdlet reads the contents of a CSV file and returns the data as a series of objects, with each line of the file representing a separate object.
- Export data from a PowerShell script to a CSV file using the Export-Csv cmdlet. This cmdlet converts the objects in an input array to CSV format and writes the resulting data to a CSV file.
- Modify the contents of a CSV file using the Import-Csv and Export-Csv cmdlets in combination with other PowerShell cmdlets and script blocks. For example, you can use the Where-Object cmdlet to filter the objects in a CSV file based on a specific criterion, or use the Sort-Object cmdlet to sort the objects in the file.
- Use the Get-Content cmdlet to read the contents of a CSV file as a string, and the Set-Content cmdlet to write a string to a CSV file. This can be useful if you want to perform text manipulation on the contents of a CSV file.
- Use the Invoke-WebRequest cmdlet to download a CSV file from a URL and save it to a local file. You can then use the Import-Csv cmdlet to read the data from the file.

## Sorting a CSV File

Suppose you have a CSV file and want to sort it. PowerShell can help!

##### Let’s generate a file first.

```
# Create an empty array to store the rows of data

$Data = @()

# Generate 100 random numbers

for ($i = 1; $i -le 100; $i++) {

  # Generate a random number between 1 and 26

  $Number = Get-Random -Minimum 1 -Maximum 26

  # Convert the number to its character equivalent

  $Character = [char]($Number + 64)

  # Create a new object with the number and character

  $Row = [pscustomobject]@{

    Number = $Number

    Character = $Character

  }

  # Add the object to the array

  $Data += $Row

}

# Export the data to a CSV file

$Data | Export-Csv -Path "C:\temp\data.csv" -NoTypeInformation
```

This script will generate 100 random numbers between 1 and 26, convert each number to its character equivalent (A-Z), and store the number and character in an object. The objects are then added to an array, which is exported to a CSV file at the specified path.

The resulting CSV file will contain two columns: “Number” and “Character”, with one row for each of the 100 random numbers.

You can customize the script as needed to generate different ranges of random numbers, or to add additional columns to the CSV file. For example, you can use the `-Minimum` and `-Maximum` parameters of the `Get-Random` cmdlet to specify a different range of numbers, or use the `Add-Member` cmdlet to add additional properties to the objects in the array.

##### Let’s sort the CSV.

Let’s sort this CSV file to return the list of numbers from lowest to highest.

```
# Import the data from the CSV file

$Data = Import-Csv -Path "C:\temp\data.csv"

# Sort the data by the Number column in descending order

$SortedData = $Data | Sort-Object -Property Number -Descending

# Output the sorted data

$SortedData
```

Notice the result is not sorted correctly.

![](assets/images/2022-12-SortedCSV.png)If the data is not sorting properly, it may be because the `Number` property is a string rather than a number. When sorting strings, the default behavior is to sort them alphabetically, which means that the string “26” would come before the string “9”.

To fix this issue, you can cast the `Number` property to a number before sorting the data. For example:

```
# Import the data from the CSV file

$Data = Import-Csv -Path "C:\temp\data.csv"

# Sort the data by the Number column in descending order

$SortedData = $Data | Sort-Object -Property Number -Descending

$Data = $Data | Sort-Object -Property { [int]$_.Number }

# Output the sorted data

$SortedData
```

This would sort the data by the `Number` property, but treat it as an integer rather than a string. This would ensure that the numbers are sorted correctly, with smaller numbers coming before larger ones.

What if you wanted to sort the characters column?

```
$Data = $Data | Sort-Object -Property Character -Descending
```

You get

![](assets/images/2022-12-SortedResult.png)