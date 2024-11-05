---
id: 802
title: 'Querying Azure Insights'
date: '2024-01-10T06:03:00-04:00'
author: jamilpremji
layout: post
guid: 'https://www.jamilpremji.com:443/?p=802'
permalink: /index.php/2024/01/10/querying-azure-insights/
burst_total_pageviews_count:
    - '7'
categories:
    - azure
    - PowerShell
---

Azure Insights and Log Analytics make sifting through logs and monitoring a beautiful experience.

```
Event 
| where tostring(EventID) matches regex @'4700|4701|5139'
| project TimeGenerated, Source, EventLog, EventID, RenderedDescription, _ResourceId

```

The query above will find all the events you need to track. Just replace the event ID with the ID’s you want.

Querying memory or CPU of a server is simple as well

```
Perf
| where ObjectName == "Memory" and CounterName == "Total MBytes Memory"
| project TimeGenerated, Computer, _ResourceId, CounterValue
| summarize avg(CounterValue) by bin(TimeGenerated, 15min), Computer, _ResourceId
| render timechart

```