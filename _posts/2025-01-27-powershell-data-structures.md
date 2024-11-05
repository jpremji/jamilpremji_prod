---
id: 62
title: 'PowerShell &#8211; Data Structures'
date: '2025-01-27T09:36:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=62'
permalink: /:year-:month-:day-:title
footnotes:
    - ''
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

In PowerShell, arrays, hashtables, and objects are data structures that can be used to store and manipulate data. Each type of data structure has its own characteristics and uses, and you can choose the one that is most suitable for your needs based on the type and amount of data you are working with.

#### Arrays

An array is a collection of elements that are stored together and accessed using an index. Arrays are useful when you need to store a large number of related items, and they are especially useful when you need to perform operations on the elements of the array, such as sorting or searching. To create an array in PowerShell, you can use the `@()` syntax, like this:

> 

```
# Create an array of strings

$array = @("apple", "banana", "orange")

# Access an element of the array

Write-Host $array[1] # Outputs "banana"
```

#### Hashtables

A hashtable is a data structure that stores key-value pairs. Hashtables are useful when you need to store data that is organized by keys, and they are particularly useful for storing data that needs to be accessed quickly, such as dictionaries or lookup tables. To create a hashtable in PowerShell, you can use the @{} syntax, like this:

```
# Create a new hashtable

$hashtable = @{}

# Add some key-value pairs to the hashtable

$hashtable.Add("Key1", "Value1")

$hashtable.Add("Key2", "Value2")

$hashtable.Add("Key3", "Value3")

# Access a value from the hashtable using its key

$value = $hashtable["Key2"]

# Output the value

Write-Output $value
```

#### Objects

An object in PowerShell is a data structure that consists of a set of properties and methods. Objects are useful when you need to represent complex data or perform operations on data, and they are especially useful when working with .NET objects or when creating custom objects in PowerShell. To create an object in PowerShell, you can use the New-Object cmdlet, like this:

```
# Create an object

$object = New-Object System.Text.StringBuilder

# Access a property of the object

Write-Host $object.Capacity # Outputs 16

# Call a method of the object

$object.Append("Hello, world!")

Write-Host $object.ToString() # Outputs "Hello, world!"
```

#### PSCustomObject

A PSCustomObject is a type of object in PowerShell that allows you to create custom objects with your own properties and methods. You can use PSCustomObjects to represent complex data or to group related data together in a way that is easy to access and manipulate.

```
# Create a PSCustomObject

$object = [PSCustomObject]@{

    "Name" = "John"

    "Age" = 30

    "Gender" = "Male"

  }

  # Access a property of the object

  Write-Host $object.Name # Outputs "John"

  # Add a new property to the object

  $object | Add-Member -MemberType NoteProperty -Name "Occupation" -Value "Software developer"

  # Access the new property

  Write-Host $object.Occupation # Outputs "Software developer"
```

In this example, we create a PSCustomObject with three properties: “Name”, “Age”, and “Gender”. We then access the “Name” property of the object and display it using the Write-Host cmdlet. Next, we add a new property called “Occupation” to the object using the Add-Member cmdlet, and then we access the new property and display its value

PSCustomObjects are very useful for organizing and manipulating data in PowerShell, and they are often used in scripts and applications to represent complex data structures or to group related data together.