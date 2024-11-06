---
id: 90
title: 'PowerShell and Functions'
date: '2024-02-16T06:03:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=90'
permalink: /:year-:month-:day-:title
burst_total_pageviews_count:
    - '1'
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
tags:
    - PowerShell
---

A function in PowerShell is a block of code that can be defined and then called by name. Functions can take input parameters and return output, just like a cmdlet. You can use functions to encapsulate a specific task or set of tasks, and then reuse that code multiple times in your script or on the command line. Here’s an example of a simple function in PowerShell:

```powershell
function Get-Greeting {

    param($Name)

    "Hello, $Name!"

  }
```

The `function` keyword is used to define the start of the function, and the `param` keyword is used to define a parameter that the function expects as input. The body of the function is the code that will be executed when the function is called, in this case, a string with the greeting is returned.

To call this function, you would use the following syntax:

```powershell

Get-Greeting -Name "John"

```

This would output the string “Hello, John!” to the console.

You can also define multiple parameters for a function, like this:

```powershell
function Get-Greeting {

    param($FirstName, $LastName)

    "Hello, $FirstName $LastName!"

  }
```

To call this function with multiple parameters, you would use the following syntax:

```powershell
Get-Greeting -FirstName "John" -LastName "Doe"
```

This would output the string “Hello, John Doe!” to the console.

You can make a parameter mandatory in a PowerShell function by using the `[Parameter(Mandatory=$true)]` attribute. For example, to make the `$FirstName` parameter mandatory in the `Get-Greeting` function, you would define the function like this:

```powershell
function Get-Greeting {

    [Parameter(Mandatory=$true)]

    param($FirstName, $LastName)

    "Hello, $FirstName $LastName!"

  }
```

Now, if you try to call the `Get-Greeting` function without specifying a value for the `$FirstName` parameter, you will get an error message telling you that the parameter is mandatory and you must provide a value.

```powershell
Get-Greeting -LastName "Doe"
```

This would produce an error message like “A parameter cannot be found that matches parameter name ‘FirstName’.”

You can use the `ValidateSet` attribute to specify a set of allowed values for a parameter in a PowerShell function. For example, to limit the `$LastName` parameter in the `Get-Greeting` function to a set of allowed values, you could define the function like this:

```powershell
function Get-Greeting {

    param($FirstName)

    [ValidateSet("Doe", "Smith", "Jones")]

    param($LastName)

    "Hello, $FirstName $LastName!"

  }
```

Now, if you try to call the `Get-Greeting` function with a value for the `$LastName` parameter that is not in the set of allowed values, you will get an error message telling you that the value is not valid.

```powershell
Get-Greeting -FirstName "John" -LastName "Brown"
```

This would produce an error message like “The value of the parameter ‘LastName’ is invalid: Brown. Valid values are: Doe, Smith, Jones.”

You can also use the `ValidateSet` attribute to specify a set of allowed values that is stored in a variable or array. For example:

```powershell
$AllowedLastNames = "Doe", "Smith", "Jones"

function Get-Greeting {

  param($FirstName)

  [ValidateSet($AllowedLastNames)]

  param($LastName)

  "Hello, $FirstName $LastName!"

}
```

This would have the same effect as the previous example, but the set of allowed values is stored in the `$AllowedLastNames` variable rather than being hard-coded in the function definition.

In the previous example for piping, we are able to pipe multiple functions, first, Get-Process, then Where-Object, and into Sort-Object, finally calling Format-Table.