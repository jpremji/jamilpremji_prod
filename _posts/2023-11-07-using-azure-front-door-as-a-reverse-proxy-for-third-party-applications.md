---
id: 790
title: 'Using Azure Front Door as a Reverse Proxy for Third Party Applications'
date: '2023-11-07T09:36:00-04:00'
author: jamilpremji
layout: post
guid: 'https://www.jamilpremji.com:443/?p=790'
permalink: /:year-:month-:day-:title
burst_total_pageviews_count:
    - '206'
categories:
    - azure
---

**1. Create an Origin Group:**

- Log in to the Azure portal ().
- In your Front Door resource, go to “Origin Groups” and create a new one.
- Add the third-party URL as a backend host within the Origin Group.

**2. Assign a Custom Domain:**

- In the Azure Front Door panel, go to “Domains.”
- Add your custom domain, “service.company.com”
- 

**3. Create an Endpoint:**

- In the Azure Front Door panel, go to “Front Door Manager”
- Add an endpoint for your custom domain.
- Set the origin group as the destination and the domain as the listening URL