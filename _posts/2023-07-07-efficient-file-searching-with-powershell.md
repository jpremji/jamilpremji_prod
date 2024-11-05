---
id: 645
title: 'Efficient File Searching with PowerShell'
date: '2023-07-07T09:21:13-04:00'
author: jamilpremji
layout: post
guid: 'https://www.jamilpremji.com:443/?p=645'
permalink: /index.php/2023/07/07/efficient-file-searching-with-powershell/
burst_total_pageviews_count:
    - '50'
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
---

To search for the string in all files within the folder “C:\\inetpub\\wwwroot” using PowerShell, you can use the `Select-String` cmdlet. Here’s an example of how you can accomplish this:

```
Get-ChildItem -Path "C:\inetpub\wwwroot\" -Recurse | Select-String -Pattern "https://"
```

1. `Get-ChildItem` retrieves all files and folders within the specified path.
2. The `-Recurse` parameter ensures that the search is performed recursively, including all subfolders.
3. The output of `Get-ChildItem` is piped (`|`) to `Select-String`.
4. `Select-String` searches for the specified pattern (“https://”) within the content of each file.
5. The command will display the lines containing the matching pattern, along with the corresponding file names.

This command will only search within text-based files (e.g., .txt, .csv, .xml).