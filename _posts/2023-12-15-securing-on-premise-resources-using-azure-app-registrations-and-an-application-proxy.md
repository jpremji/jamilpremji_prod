---
id: 641
title: 'Securing On-Premise Resources Using Azure App Registrations and an Application Proxy'
date: '2023-12-15T18:03:00-04:00'
author: jamilpremji
layout: post
guid: 'https://www.jamilpremji.com:443/?p=641'
permalink: /index.php/2023/12/15/securing-on-premise-resources-using-azure-app-registrations-and-an-application-proxy/
burst_total_pageviews_count:
    - '2'
image: /wp-content/uploads/2023/01/pngwing.com1_.png
categories:
    - azure
---

1. Azure Active Directory (AAD) Setup: 
    - If you don’t have an Azure AD tenant, create one in the Azure portal.
2. Application Proxy Setup: 
    - Install and configure the Azure AD Application Proxy connector on at least two servers within your on-premises network to ensure high availability.
    - Configure the connector to establish a secure outbound connection to the Azure AD service.
    - Open the necessary firewall ports to allow communication between the Application Proxy connectors and the Azure AD service.
3. Application Proxy Portal Configuration: 
    - Access the Application Proxy portal in the Azure portal.
    - Create a new enterprise application for your on-premises application.
4. App Registration: 
    - In the enterprise application configuration, configure the redirect URI to the internal URL of your on-premises application.
    - This step ensures that authentication requests are directed to the appropriate location.
5. Enterprise Application: 
    - In the enterprise application configuration, under the Application Proxy section, set the internal URL of your on-premises application.
    - This URL needs to be accessible to the internal servers hosting the application.
6. DNS Configuration: 
    - Set up DNS records using public DNS to map the external URL of the application to the Azure AD Application Proxy.
7. Access Control: 
    - Under the Properties section of the enterprise application configuration, set “Assignment Required” to Yes.
    - This setting ensures that users and groups must be assigned access to the application.
8. Users and Groups: 
    - In the Users and Groups section, assign the appropriate users and groups who should have access to the application.
    - This step controls who can access the published application through Azure AD.

It’s important to note that the specific configuration details may vary depending on your environment and requirements. Make sure to consult Microsoft’s official documentation for detailed instructions on setting up Azure AD Application Proxy and configuring the various settings mentioned above.