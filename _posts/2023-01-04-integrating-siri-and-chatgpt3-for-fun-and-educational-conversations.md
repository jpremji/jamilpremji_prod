---
id: 227
title: 'Integrating Siri and ChatGPT3 for Fun and Educational Conversations'
date: '2023-01-04T22:13:29-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=227'
permalink: /:year-:month-:day-:title
burst_total_pageviews_count:
    - '64'
image: /wp-content/uploads/2023/01/getcontent-1.png
categories:
    - chatgpt3
tags:
    - chatgpt3
    - openai
---

<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" frameborder="0" height="281" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/PBCH_RxNd2A?feature=oembed" title="Bringing AI to the Table: Integrating Siri and ChatGPT/ChatGPT3" width="500">In order to get Siri to talk to ChatGP3, you need an OpenAI account. Login to OpenAI and [generate your API key](https://beta.openai.com/account/api-keys).</iframe>

1. 

Once you have your API key, launch the Shortcuts App on your phone.

![Index](../assets/images/2023-01-index.jpg)

2. 
Click the + to create a new shortcut

![New](assets/images/2023-01-WhatsApp-Image-2023-01-04-at-4.41.01-PM1.jpeg)3. 

For your first action, choose **Ask for Input**.

![](assets/images/2023-01-WhatsApp-Image-2023-01-04-at-4.45.56-PM.jpeg)4. 

It should say **Ask for** “***Text***” **with** “***Ask ChatGPT3?***” This is what Siri will ask you when you call this shortcut.

![](assets/images/2023-01-WhatsApp-Image-2023-01-04-at-4.41.01-PM3-Copy.jpeg)5. 

At the bottom where it says “Search for Apps and Actions” type in **Set Variable**

![](assets/images/2023-01-WhatsApp-Image-2023-01-04-at-5.10.04-PM1.jpeg)6. 

Set Variable to “Prompt” to “Provided Input”

![](assets/images/2023-01-WhatsApp-Image-2023-01-04-at-1.56.28-PM2-Copy.jpeg)7. 

At the bottom, choose **Get Contents From URL**

![](assets/images/2023-01-WhatsApp-Image-2023-01-04-at-5.10.04-PM.jpeg)8. 

Type in the URL in the open space: **https://api.openai.com/v1/completions**

![](assets/images/2023-01-getcontent.png)9. 

Click the blue arrow and make yours look similar. The only difference is after Bearer in the “Authorization” key, you need to paste the [API key you generated from OpenAI](https://beta.openai.com/account/api-keys).

![](assets/images/2023-01-WhatsApp-Image-2023-01-04-at-1.56.28-PM-2.jpeg)11. 

Type in get dictionary from “**Contents of URL**“

![](assets/images/2023-01-getdictionaryinput-2.jpeg)12. 

Set it to the following

![](assets/images/2023-01-getdictionaryfromurl.png)13. 

Type in “Get Dictionary Value”

![](assets/images/2023-01-getdicvalue.jpeg)14. 

Get “Value” for “Choices” in “Dictionary”

![](assets/images/2023-01-getvalueforchoice.png)15. 

Search “Get Dictionary From”

![](assets/images/2023-01-getdictionaryinput.jpeg)16. 

Set it to “Dictionary Value”

![](assets/images/2023-01-getdicvalue2.png)17. 

Search **Dictionary From Input**

![](assets/images/2023-01-getdictionaryinput.jpeg)18. 

Set it to: Get “Value for “Text” in “Dictionary”

![](assets/images/2023-01-getvaluefortext.png)19. 

Search “Speak Text”

![](assets/images/2023-01-65116-576x1024.jpg)20. 

Set it to Speak “Dictionary Value”

![](assets/images/2023-01-speak-1.png)#### At the top of the screen, set the name of the shortcut to OpenChat.

#### Now ask Siri for Open Chat and you will be prompted with Ask ChatGPT3?

This is how it all looks.

![](assets/images/2023-01-WhatsApp-Image-2023-01-04-at-1.56.28-PM2-1.jpeg)![](assets/images/2023-01-WhatsApp-Image-2023-01-04-at-1.56.28-PM1.jpeg)![](assets/images/2023-01-WhatsApp-Image-2023-01-04-at-1.56.28-PM-1.jpeg)## TL:DR

If you want to avoid doing all the work, you can [install this Shortcut.](https://www.icloud.com/shortcuts/90e2d0cbe7014d52ab1e425d5d15dbce)

Scroll down to the “Get Content from https://” and hit the blue arrow. Scroll down to Authorization and replace “yourtoken” with [your API token](https://beta.openai.com/account/api-keys).

![](assets/images/2023-01-getcontent-1.png)![](assets/images/2023-01-header.jpeg)