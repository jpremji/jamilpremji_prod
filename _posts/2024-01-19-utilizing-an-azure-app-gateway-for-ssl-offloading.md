---
id: 682
title: 'Utilizing An Azure App Gateway for SSL Offloading'
date: '2024-01-19T06:03:00-04:00'
author: jamilpremji
layout: post
guid: 'https://www.jamilpremji.com:443/?p=682'
permalink: /index.php/2024/01/19/utilizing-an-azure-app-gateway-for-ssl-offloading/
burst_total_pageviews_count:
    - '2'
categories:
    - azure
---

- Create an App Gateway in Azure
- Configure the listener to listen on port 80 or 443 
    - If you create a port 80 listener and change it to 443, you have to delete and re-create it and visa-versa.
- Upload an SSL certificate for port 443 to the gateway
- Configure the backend pool to point to the application 
    - Use port 80 for offloading
- Create a health check and apply it to the listener
- Apply the backend to the routing rule
- 