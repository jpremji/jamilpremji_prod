---
id: 49
title: 'How Do I Use Variables in PowerShell'
date: '2024-04-01T01:37:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=49'
permalink: /:year-:month-:day-:title
burst_total_pageviews_count:
    - '8'
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---
![Image](assets/images/powershell.png)

In PowerShell, a variable is a container that stores a value or reference to an object. You can use variables to store and manipulate data, and to pass data between commands and scripts. To use variables in PowerShell, follow these steps:

1. Declare a variable: To create a new variable in PowerShell, you can use the `$` symbol followed by the name of the variable. For example, to create a new variable called `$message`, you can type `$message =`.
2. Assign a value to a variable: To assign a value to a variable, you can use the `=` operator followed by the value you want to assign. For example, to assign the string “Hello, world!” to the `$message` variable, you can type `$message = "Hello, world!"` and press Enter.
3. Use a variable: To use a variable in a command or script, you can simply refer to the variable by its name. For example, to display the value of the `$message` variable, you can use the `Write-Host` cmdlet like this: `Write-Host $message`.

```powershell
# Declare a variable and assign it a value
$message = "Hello, world!"

# Use the variable in a command
Write-Host $message

```

### Write-Host Versus

Write-Host is a cmdlet in PowerShell that is used to display output in the console window. While Write-Host can be useful for displaying simple messages or debugging output, it is generally not recommended for use in production scripts or applications because it has some limitations and drawbacks compared to other methods of displaying output.

Some of the reasons why you might not want to use Write-Host include:

1. It is not suitable for displaying structured data: Write-Host is designed for displaying simple strings of text. It does not support displaying structured data such as objects, arrays, or lists in a way that is easy to parse or manipulate.
2. It is not suitable for redirecting output: Write-Host writes its output directly to the console window and cannot be redirected to other streams or files using redirection operators such as `>` or `|`. This means that it is not possible to capture or save the output of Write-Host for later use.
3. It does not support formatting: Write-Host does not support formatting options such as color, font, or background color, which can make it difficult to display output in a visually appealing or easy-to-read way.
4. It can interfere with the output of other commands: Because Write-Host writes its output directly to the console window, it can interfere with the output of other commands that are being run in the same session. This can make it difficult to understand what is happening in a script or application that uses Write-Host.

In general, it is recommended to use other methods of displaying output in PowerShell scripts and applications, such as Write-Output, Write-Verbose, or Write-Error. These cmdlets allow you to display output in a more flexible and customizable way, and they also support redirection and formatting options.

### Enforcing Data Types

Enforcing datatypes in PowerShell is important because it helps to ensure that your code is consistent and reliable. When you declare a variable with a specific datatype, you are telling PowerShell what kind of data the variable is expected to hold. This helps to prevent errors that can occur when you try to use a variable in a way that is incompatible with its datatype.

For example, suppose you have a script that calculates the area of a rectangle. You might define a variable `$length` to represent the length of the rectangle, and another variable `$width` to represent the width. If you declare `$length` and `$width` as integers, you can be sure that they will always hold whole numbers. This means that you can perform mathematical operations on them without having to worry about decimal values or rounding errors.

```powershell
# Declare variables as integers
[int] $length = 5

[int] $width = 10

# Calculate the area of the rectangle
$area = $length * $width

# Output the result
Write-Output "The area of the rectangle is $area."
```

In this example, the variables `$length` and `$width` are declared as integers using the `[int]` type accelerator. This ensures that they can only hold whole numbers, which makes it easier to perform calculations on them. If you tried to assign a decimal value to either of these variables, PowerShell would generate an error.

![](assets/images/2022-12-EnforceDataType.png)