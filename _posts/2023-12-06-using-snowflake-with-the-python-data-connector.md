---
id: 677
title: 'Using SnowFlake with the Python Data Connector'
date: '2023-12-06T21:36:00-04:00'
author: jamilpremji
layout: post
guid: 'https://www.jamilpremji.com:443/?p=677'
permalink: /index.php/2023/12/06/using-snowflake-with-the-python-data-connector/
footnotes:
    - ''
burst_total_pageviews_count:
    - '7'
categories:
    - python
    - snowflake
tags:
    - azure
    - python
    - snowflake
---

To use Python and SnowFlake you need the data connector

```
pip install snowflake-connector-python
```

This code block would run a basic select statement

```
import snowflake.connector
ctx = snowflake.connector.connect(
    user='datadog_user',
    password='xxx',
    account='ORG-REGION'
    )
cs = ctx.cursor()
try:
    cs.execute("Select * From *")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()

```

To [encrypt your password see this post](http://sending-an-e-mail-using-python-and-office365-smtp).