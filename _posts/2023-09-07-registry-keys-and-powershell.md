---
id: 138
title: 'Registry Keys and PowerShell Uninstall Strings'
date: '2023-09-07T16:53:41-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=138'
permalink: /:year-:month-:day-:title
footnotes:
    - ''
burst_total_pageviews_count:
    - '172'
categories:
    - PowerShell
tags:
    - PowerShell
---

To search the registry for the uninstall strings of both x64 and regular applications using PowerShell, you can use the `Get-ChildItem` cmdlet to enumerate the keys in the registry and the `Get-ItemProperty` cmdlet to retrieve the values of the keys.

For example, the following command searches the registry for the uninstall strings of x64 applications:

```powershell
$UninstallStrings = Get-ChildItem 'HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall' |

                    Get-ItemProperty |

                    Where-Object { $_.DisplayName -and ($_.SystemComponent -eq $False) } |

                    Select-Object DisplayName, UninstallString
```

This command retrieves all keys under the `HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall` key and then uses the `Get-ItemProperty` cmdlet to retrieve the values of the keys. It filters the keys by checking for the presence of a `DisplayName` value and the absence of a `SystemComponent` value, and then selects the `DisplayName` and `UninstallString` values.

To search for the uninstall strings of regular (x86) applications, you can use a similar command, but specify the `HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall` key instead:

```powershell
$UninstallStrings = Get-ChildItem 'HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall' |

                    Get-ItemProperty |

                    Select-Object DisplayName, UninstallString
```

This command searches the registry for the uninstall strings of regular (x86) applications by enumerating the keys under the `HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall` key and filtering the keys in the same way as the previous example.

The resulting `$UninstallStrings` variable will contain a list of objects, with each object representing an application and containing the `DisplayName` and `UninstallString` values for the application.

Keep in mind that these commands assume that the registry keys and values are correctly formatted and can be accessed using the `Get-ChildItem` and `Get-ItemProperty` cmdlets. If the keys or values are not in the expected format, these cmdlets may not work as intended.

### CD HKCU:

The `cd` command in PowerShell allows you to change the current directory or location. The `hkcu:` notation stands for “HKEY\_CURRENT\_USER”, which is a predefined registry hive that refers to the current user’s registry key. It is one of several predefined registry hives in the Windows Registry, which are used to store configuration information for the operating system, applications, and users.

To view the registry from PowerShell, you can use the `Get-ChildItem` cmdlet with the `hkcu:` location. For example, the following command will list the subkeys under the HKEY\_CURRENT\_USER hive:

```powershell
cd hkcu:

Get-ChildItem
```

You can also use the `Get-ItemProperty` cmdlet to view the properties of a specific registry key. For example, the following command will display the properties of the HKEY\_CURRENT\_USER\\Control Panel\\Desktop key:

```powershell
cd ‘hkcu:\Control Panel\Desktop’

Get-ItemProperty .
```

You can also use the `Set-ItemProperty` cmdlet to modify the values of a specific registry key. For example, the following command will set the value of the “Wallpaper” property to “C:\\Wallpaper.jpg”:

```powershell
cd hkcu:\Control Panel\Desktop

Set-ItemProperty . -Name Wallpaper -Value "C:\Wallpaper.jpg"
```

It’s important to note that modifying the registry can have serious consequences if not done carefully. It is recommended to make a backup of the registry before making any changes.