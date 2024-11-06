---
id: 636
title: 'AZ-305: Designing Microsoft Azure Infrastructure Solutions'
date: '2023-06-09T17:27:10-04:00'
author: jamilpremji
layout: post
guid: 'https://www.jamilpremji.com:443/?p=636'
permalink: /:year-:month-:day-:title
burst_total_pageviews_count:
    - '150'
image: /wp-content/uploads/2023/01/pngwing.com1_.png
categories:
    - azure
---

## Azure Services:

1. Azure Data Factory (ADF): Used for creating pipelines, loading data, and controlling activities.
2. Azure Cache for Redis: Provides a caching solution.
3. Azure Logic Apps and Functions: Logic Apps require a data gateway for on-premise integration, while Functions need premium for VNet connectivity.
4. Azure Data Lake Storage (ADLS): Allows data ingestion for long-term storage.
5. Azure Synapse Analytics (formerly SQL Data Warehouse): Supports transaction data, daily jobs, analysis on stored SQL data, and development of notebooks.
6. Azure Cosmos DB: Stores data in JSON-like format, supports SQL queries, low latency, multi-region writes, and provides a SQL DB API and Time Series Insight.
7. Azure CycleCloud: Used for implementing high-performance computing (HPC) workloads.
8. Azure Service Fabric: Enables independent upgrades of microservices.
9. Azure Key Vault: Stores and manages cryptographic keys, secrets, and certificates.
10. Azure SQL Managed Instance (SQL MI): Offers high-capacity storage for OLTP, but doesn’t support cross-database queries.
11. Azure Monitor: Provides alerts for monitoring.
12. Azure AD Connect Health: Checks the health of AD Connect.
13. Azure Blueprint: Allows you to define and assign configurations to deployed resources.
14. Azure Active Directory Domain Services (ADDS): Provides domain services.
15. Azure Queue Storage: Enables communication using XML.
16. Azure Application Insights: Used for in-app monitoring.
17. Azure Resource Mover: Moves virtual machines (VMs) between regions.
18. Azure Pipeline Release Pipelines: Supports building and deploying images to Azure Container Registry (ACR) and Azure Kubernetes Service (AKS).
19. Azure Blob Storage: Offers tiering and has a capacity of up to 4.77TB.
20. Azure Policy: Can be applied to subscriptions, resource groups, and management groups.

## Concepts and Features:

1. Self-Hosted Integration Runtime: Used in Azure Data Factory for on-premise integration.
2. Data Path Availability: Ensures availability of data paths in a system.
3. SYN Count: Represents the number of SYN packets in a network communication.
4. Database Transaction Units (DTUs): Measure the performance of an Azure SQL Database.
5. Long-Term Retention: Required to retain data for 7 years in Azure SQL Database.
6. Gremlin: Query language for Apache TinkerPop graph databases.
7. VHD Files: Used for SQL Database and can reduce failover time using Distributed Network Name (DNN).
8. Auto Sending Logs to Azure SQL: Azure SQL has a premium tier for redundant replicas.
9. Azure Synapse Link for Azure Cosmos DB: Allows data analysis without impacting database performance.
10. Soft Delete: A feature that allows the recovery of deleted data.
11. Hierarchical Namespaces: Organizational structure for managing Azure resources.
12. Single Sign-On (SSO): Supported through App Proxy, Enterprise Applications, and Conditional Access.
13. Priority Traffic Routing: Handled by Azure Traffic Manager.
14. Azure AD Entitlement Management: Used to govern external users’ access rights.
15. Azure Service Bus: Supports processing XML messages, topics, queues, and sessions.
16. Azure Log Analytics: Provides subscription-related information.
17. Microsoft Identity Platform: Manages tokens for identities.
18. Cluster Autoscaler: Part of Azure Container Instances (ACI) to scale AKS by offloading Pods.
19. Horizontal Scaler: Monitors metrics to scale resources.
20. Dynamic Data Masking: Masks sensitive data in databases.
21. Data Migration Assistant: Facilitates offline migrations of SQL Server servers starting from SQL Server 2012. 22. High-Performance Compute: H16r is an example of a high-performance compute instance, and Remote Directory Memory Access (RDMA) is used for efficient memory access.

23. Azure Identity Governance: An alternative to Privileged Identity Management (PIM) for identity governance.
24. Application Gateway: Includes an Ingress Controller (APIC) for managing inbound traffic to applications.
25. Password-Based SSO: Enables single sign-on for applications that don’t support identity providers.
26. Azure Instance Metadata Service Identity: Used for obtaining VM tokens.

## Other Points:

- Load balancing can be achieved with Azure Load Balancer, which can be global.
- Bounded staleness provides strong consistency for databases.
- Smart lockout is used to prevent brute force attacks.
- Legacy authentication can be stopped using conditional access policies.
- Web Application Firewall (WAF) and Azure Front Door support connection limits.
- Azure Database Migration Service enables offline migrations of servers.
- Azure AD entitlement management is useful for governing external users’ access rights.
- Azure Policy can be applied at the subscription, resource group, and management group levels.
- Azure Monitor is responsible for sending alerts, while Application Insights is used for in-app monitoring.
- Azure Data Lake Storage (ADLS) can ingest data for long-term storage, and Blob Storage can also be used for this purpose.
- Azure Resource Mover facilitates the movement of VMs between regions.
- RA-GRS (Read-Access Geo-Redundant Storage) and SAS (Shared Access Signature) keys are used for Azure Storage.
- Azure Pipeline Release Pipelines support the building and deployment of ACR images to AKS.
- NC, DS, and NV are VM series types in Azure.
- Azure App Proxy, Enterprise App, and Conditional Access policies can be used for single sign-on of on-premises apps.
- Azure Firewall Parent and Child Policies must be in the same region.
- BlockBlobStorage is a premium storage option suitable for high-transaction scenarios.
- Caching log files is unnecessary, and setting data as read-only for caching can improve transaction speed.
- Resource locks can be used to prevent changes to an application for a specific period of time.
- Stored access policies can be used for data compliance.
- The CAF (Cloud Adoption Framework) includes the stages of Assess, Deploy, and Release.
- App Registrations can be used to avoid login prompts for internal corporate applications.
- Azure Service Bus supports processing XML messages, and Azure Event Grid and Azure Event Hubs are alternative options.
- AVRO is the format used for Event Hubs Capture to receive data.
- Azure SQL Diagnostics can be streamed to Log Analytics, SQL Analytics, Event Hubs, and Azure Storage. Multiple settings can be configured.
- Azure Identity Governance is used instead of PIM for certain reasons.
- Azure Instance Metadata Service Identity is used for obtaining VM tokens.

1. Azure Synapse Analytics (formerly SQL Data Warehouse) allows the development of notebooks for multiple programming languages.
2. Azure Cosmos DB replicates data across regions and provides four times redundancy within a region.
3. Azure Synapse Link for Azure Cosmos DB allows data analysis without impacting the performance of the database.
4. Azure SQL Managed Instance (SQL MI) has limitations in working with cross-database queries.
5. Azure Key Vault integrations can be configured in application settings, and backups are performed in the same geographical region.
6. Azure Data Factory (ADF) can be used to move files from on-premise to storage containers by using ADF and an Import/Export job.
7. Azure Blob Storage has the ability to perform tiering and has a capacity of 4.77TB.
8. Azure Data Lake Storage (ADLS) can be used to ingest data for long-term storage and can be analyzed and queried without ingesting the data.
9. Azure AD Connect Health is used to check the health of Azure AD Connect.
10. Azure Policy allows for policy definitions that have “deployIfNotExists” and can be assigned through policy assignment and remediation.
11. Azure ACI (Azure Container Instances) includes a cluster autoscaler that allows for scaling AKS (Azure Kubernetes Service) by offloading pods.
12. Azure Instance Metadata Service Identity is used for obtaining VM tokens.

1. Azure AD Logs can be sent to Event Hubs through Functions into and Cosmos DB for processing and analysis.
2. Azure SQL Database Hyperscale is optimized for online transaction processing (OLTP) and high throughput, supporting up to 100TB of data.
3. Azure SQL Database has a maximum retention period of 730 days (2 years) for backups.
4. Soft Delete is a feature that allows for the recovery of deleted data in Azure services.
5. Azure Service Fabric enables independent upgrades of microservices, supports stateful and stateless services, and provides cluster management and health monitoring.
6. Priority Traffic Routing is managed by Azure Traffic Manager, which routes traffic based on priority rules and policies.
7. Azure Service Endpoints can be used to reduce latency and secure Azure resources by enabling direct network access between virtual networks and supported Azure services.
8. Azure Database Migration Service enables online and offline migrations of on-premises databases to Azure.
9. Azure Pipeline Release Pipelines support the building of container images in Azure Container Registry (ACR) and deploying them to Azure Kubernetes Service (AKS).
10. Azure Firewall Parent and Child Policies need to be located in the same Azure region for proper functionality.
11. Azure Blob Storage supports various tiers, including hot, cool, and archive, for cost-effective storage options based on data access frequency.
12. Azure AD Entitlement Management provides a centralized way to manage and govern external users’ access to resources and applications.
13. Azure Instance Metadata Service Identity (IMDS) allows for obtaining tokens for Azure VMs to authenticate against Azure services.
14. Azure Data Factory (ADF) allows you to create pipelines for data movement, transformation, and control activities.
15. Azure Data Factory can integrate with Azure Databricks and Azure Synapse Analytics (formerly SQL Data Warehouse) for advanced data processing and analytics.
16. Azure Data Factory can be used to automatically send logs to Azure SQL Database for storage and analysis.
17. Azure Cosmos DB stores data in a JSON-like format and supports SQL queries with low latency.
18. Azure Table Storage with Geo-Zone Redundant Storage (GZRS) can provide multiple-region write capability, similar to Azure Cosmos DB.
19. Azure Cosmos DB Data Migration Tools can be used to migrate data to Azure Cosmos DB, including support for MongoDB migrations.
20. Azure Synapse Analytics supports transactional data processing, daily job scheduling, analysis on stored SQL data, and the development of notebooks for multiple programming languages.
21. Azure Key Vault is a secure storage service that allows you to manage and safeguard cryptographic keys, secrets, and certificates.
22. Azure Service Bus supports messaging patterns using queues and topics, with options for session-based message processing and FIFO (First-In-First-Out) delivery.
23. Azure Application Gateway includes an Ingress Controller (APIC) for managing inbound traffic to applications.
24. Azure SQL Database offers features such as dynamic data masking for sensitive data protection and Always Encrypted for secure data encryption.
25. Azure SQL Managed Instance (SQL MI) has specific capacity limits, including maximum CPU cores and allotted storage, with different performance tiers available.
26. Azure Firewall can enforce network-level filtering rules to control inbound and outbound traffic to and from Azure resources.
27. Azure DevOps Release Pipelines enable the deployment of container images built in Azure Container Registry (ACR) to Azure Kubernetes Service (AKS).
28. PolyBase can be used to move data from Azure Data Lake Storage (ADLS) to Azure Stream Analytics (ASA) for analysis.

![](assets/images/2023-09-image-1.png)