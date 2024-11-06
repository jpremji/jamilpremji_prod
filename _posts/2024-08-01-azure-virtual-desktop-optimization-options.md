---
id: 853
title: 'Azure Virtual Desktop Optimization Options'
date: '2024-08-01T21:52:47-04:00'
author: jamilpremji
layout: post
guid: 'https://www.jamilpremji.com:443/?p=853'
permalink: /:year-:month-:day-:title
burst_total_pageviews_count:
    - '34'
categories:
    - Uncategorized
---

So you want to replace your Citrix farm. You roll out Azure Virtual Desktop. Deploy the image. Get users logged on. It just works. However, like Citrix, AVD has quirks also. These are the challenges I have run into AVD.

1. You need to run FSLogix. Sometimes it acts up but its great in comparison to legacy profile management.
2. [FSLogix has a clean up script, it’s a godsend to help save storage space and keep profiles clean.](https://github.com/FSLogix/Invoke-FslShrinkDisk) The larger the profile, the longer it takes to mount, therefore slower logons.
3. Latency matters. Users in India will take longer to logon if you have resources in East US and they are on hotspots
4. [Install Teams for VDI. ](https://learn.microsoft.com/en-us/windows-365/enterprise/create-custom-image-support-teams) Install WebRTC and set the key.
5. Use a GPU to reduce CPU usage. One user per core works with GPUs but not CPU power only
6. AVD needs RAM – E series if you don’t want N series
7. The [AVD app wo](https://aka.ms/AVDStoreClient)rks or the [MSI](https://learn.microsoft.com/en-us/azure/virtual-desktop/users/connect-windows?pivots=remote-desktop-msi)
8. The [Windows App is the future ](https://apps.microsoft.com/detail/9N1F85V9T8BN)
9. Some apps are greedy and can slow down other users on the server
10. The network card saturates if too many people are hitting the same endpoint, so reduce sessions counts per server if you see a bottleneck
11. Each pool should have its own log analytics workspace
12. Premium storage as it runs faster
13. Page files, which are managed help as sometimes someone can use all the RAM up with their applications
14. If an app crashes, or if apps are crashing, the VM is undersized
15. Update the FSLogix Version, however, every update has its own challenges. Will discuss stuck profiles.
16. If sessions are getting stuck on a server, reboot it. 
    - Create a script to look for active sessions and compare against mounted profiles. If a VHD is mounted, that means the log-off failed in a timely manner.
    - If multiple drives are mounted on a server without a session in AVD, the server needs to be put on drain mode