---
id: 806
title: 'Replacing Citrix with Azure AVD'
date: '2024-01-01T06:03:00-04:00'
author: jamilpremji
layout: post
guid: 'https://www.jamilpremji.com:443/?p=806'
permalink: /index.php/2024/01/01/replacing-citrix-with-azure-avd/
burst_total_pageviews_count:
    - '14'
categories:
    - azure
---

Citrix is indeed a powerful platform that offers virtual desktop infrastructure (VDI) and application delivery solutions to organizations. It provides a range of features and capabilities that can be valuable for businesses, including:

1. **VDI Environment**: Citrix allows organizations to create and manage virtual desktop environments, which can be accessed by users from various devices, providing flexibility and mobility.
2. **Application Delivery**: It enables efficient and secure application delivery to users, ensuring that they can access the applications they need, regardless of location.
3. **Load Balancing with Netscalers**: Citrix NetScaler is a load balancing and application delivery controller that optimizes application performance and ensures high availability.
4. **Auto Scaling**: Citrix can help organizations implement auto-scaling strategies, allowing for resource allocation based on demand, which can be cost-effective.
5. **Cloud Connectors**: These connectors facilitate integration between on-premises infrastructure and cloud services, enhancing flexibility and enabling hybrid cloud deployments.

While Citrix offers a robust solution, as mentioned, it also comes at a cost. Organizations should carefully consider their needs and budget before implementing Citrix or any similar platform. Additionally, as organizations modernize and migrate to cloud-native and more cost-effective solutions, they may find that their dependency on VDI and traditional Windows systems decreases, which can lead to cost savings.

It’s essential for organizations to regularly assess their IT infrastructure and align their technology stack with their current and future business requirements to optimize costs and enhance efficiency. Transitioning from traditional systems to more modern, cloud-based solutions can be a strategic move for many organizations, offering both cost savings and increased agility.

Transitioning from Citrix to Azure Virtual Desktop (AVD) can be a strategic move for organizations looking to save on licensing costs and streamline their virtual desktop infrastructure. Here are the key steps and considerations for making this transition:

1. **Identify the Number of Users**: 
    - Determine the total number of users who require access to virtual desktops and applications. Understanding your user base is essential for planning the AVD deployment.
2. **Identify the Basic Requirements**: 
    - Define the specific requirements for your virtual desktop environment, including the type of applications, performance expectations, and any compliance or security considerations.
3. **Identify How Everything Will Be Accessed**: 
    - Determine how users will access the AVD environment. Will they access it using a web browser, or the remote desktop windows 10 client?
4. **Profile Management**: 
    - Decide on the profile management strategy. Shared profiles, where user settings are carried across multiple systems, can be achieved with solutions like FSLogix. Ensure that you have a plan for managing user profiles effectively.

The initial consideration revolves around profile management in your AVD setup. Opting for shared profiles empowers your users to seamlessly carry their settings across different systems, fostering a consistent experience. To facilitate this, enabling FSLogix is the recommended approach. Notably, FSLogix comes pre-installed on Windows 10 and Windows 11 Multi-Host images, making it a convenient choice for profile management within your AVD environment.

- Create a resource group
- Create a storage account in the resource group
- Premium is 18s faster for logon times from my testing on a 32GB/8CPU server.
- Create a file share within the Storage Account
- Enable AD Authentication for the storage account 
    - This requires running the [AZFilesHybrid.psd1](https://github.com/Azure-Samples/azure-files-samples/blob/master/AzFilesHybrid/AzFilesHybrid.psd1)
- Create a security group for the users who will be logging in to create their profiles
- Add the group to the Storage File Data SMB Share Contributor role
- [Map the directory and set NTFS permissions to restrict users from accessing other profile directories](https://learn.microsoft.com/en-us/azure/virtual-desktop/fslogix-profile-container-configure-azure-files-active-directory?tabs=adds)
- Create an AVD Host Pool
- Create an Application Group 
    - The friendly name is a feature to look for
- Create a Workspace Group 
    - The friendly name is a feature to look for
- Create a VM and attach it to your host pool

That was straight forward, but you can go a step further.

- Deploy an Azure Image Gallery
- Create a Definition
- Create a brand new VM and install the software you want for your base image
- Take a snapshot and save it for future changes
- Sysprep and remove the panther directory. Use the Azure command after the server stops, and set it to Generalized.
- Capture the VM into your image definition
- Deploy this new image to your AVD host pool and fill in all the required info
- Choose the number of VM’s you want.

Now that you are running in Azure, we need to optimize our environments.

- Clean up storage profiles that aren’t being used
- Setup a scaling policy
- Terminate user sessions and implement a reboot schedule

If you want instructions with screenshots, [this article d](https://virtual-dba.com/blog/setting-up-fslogix-with-azure-virtual-desktop/)oes an impressive job.