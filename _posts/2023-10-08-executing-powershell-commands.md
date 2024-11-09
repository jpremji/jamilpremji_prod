---
id: 42
title: 'Executing PowerShell Commands'
date: '2023-10-08T09:36:00-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=42'
permalink: /:year-:month-:day-:title
burst_total_pageviews_count:
    - '27'
categories:
    - PowerShell
---

To enter and execute commands in PowerShell, follow these steps:

1. Open PowerShell: To open PowerShell, click the Start button, type “PowerShell” into the search bar, and then click on the PowerShell icon that appears. Alternatively, you can open a Command Prompt window and then type “powershell” (without the quotes) and press Enter to launch PowerShell.
2. Type a command: Once PowerShell is open, you can type a command and press Enter to execute it. For example, you can type “Get-Process” and press Enter to see a list of all the processes running on your computer.
	   ![](assets/images/2022-12-Get-Process.png)


3. Use parameters: Many PowerShell commands accept parameters that allow you to customize their behavior. To specify a parameter, you can type the name of the parameter followed by a colon and the value you want to use. For example, you could type “Get-Process -Name ‘explorer'” to see only the processes with the name “explorer”.

	![](assets/images/2022-12-Get-ProcessParam.png)
1. Use the up and down arrow keys: You can use the up and down arrow keys to navigate through the command history and recall previously entered commands. This can be useful if you want to execute the same command multiple times or if you want to modify a command you previously entered.

#### Code Editor

There are several code editors that are commonly used for PowerShell, including:

1. Visual Studio Code (VSCode): This is a popular code editor that is available for free and has many features that make it well-suited for PowerShell development, including IntelliSense, debugging, and integration with Git.
2. PowerShell ISE: This is a built-in code editor for PowerShell that is included with Windows. It has a simple interface and is a good choice for beginners. 
    1. ISE does not work with PowerShell 7
3. Notepad++: This is a free code editor that is popular for its syntax highlighting and support for multiple languages, including PowerShell.

Ultimately, the best code editor for PowerShell will depend on your personal preferences and the specific needs of your project. It’s a good idea to try out a few different options to see which one you like best.