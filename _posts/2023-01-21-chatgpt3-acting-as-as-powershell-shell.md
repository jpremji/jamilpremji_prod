---
id: 337
title: 'ChatGPT3 acting as as PowerShell Shell'
date: '2023-01-21T15:17:43-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=337'
permalink: /:year-:month-:day-:title
burst_total_pageviews_count:
    - '29'
image: /wp-content/uploads/2023/01/pngwing.com1_.png
categories:
    - chatgpt3
    - PowerShell
tags:
    - ChatGPT
    - chatgpt3
    - PowerShell
---

Recently, [I discovered a post on LinkedIn](https://dfinke.github.io/powershell,%20chatgpt/2023/01/15/Running-PowerShell-Inside-ChatGPT.html) where a [Doug Finke](https://www.linkedin.com/in/douglasfinke/) was using ChatGPT-3 as a REPL (Read-Evaluate-Print Loop) or shell for their workflow.

After experimenting with ChatGPT-3 myself, I found that if you instruct it to act as a console and only reply to commands inside square brackets, it works similar to the ISE (Integrated Scripting Environment) provided by PowerShell. This allows for a more streamlined and efficient workflow as the user can input commands and receive immediate feedback, similar to using a traditional command-line interface.

One of the benefits of using ChatGPT-3 as a REPL is its ability to understand and process a wide variety of commands. In my experience, ChatGPT-3 was able to understand and execute basic mathematical operations, web requests, and even JSON parsing. Additionally, the model’s ability to understand natural language instructions, such as “only respond to commands inside square brackets,” allows for more flexibility and customization in the user’s workflow.

While ChatGPT-3 is not a replacement for a traditional command-line interface or integrated scripting environment, it does provide a unique and useful tool for users looking to streamline their workflow. Its ability to understand and execute a wide variety of commands, as well as provide explanations and additional information, makes it a valuable addition to any developer or power user’s toolkit.

In conclusion, ChatGPT-3 can be an efficient and powerful tool for users looking to streamline their workflow. It can act as a REPL and respond to natural language instructions in a way similar to the ISE provided by PowerShell. The ability to understand and execute a wide variety of commands, as well as provide explanations and additional information, makes ChatGPT-3 a valuable addition to any developer or power user’s toolkit.

Here is an example of it doing Math as a PWSH Shell. My inputs are in Green and the responses are in Orange.

![](assets/images/2023-01-firefox_U7k4sWFjof-1024x504.png)```
"Act as a PowerShell REPL. My follow-up responses will all be REPL commands. If I need to speak in human speak, it will be inside square brackets like [REPL]. Do you understand?"

//Yes, I understand. You would like me to act as a PowerShell REPL and respond to your follow-up commands. If you need to speak in human language, it will be inside square brackets.

"$a = 3
$b = 9
$a*$b"

//27


```

![](assets/images/2023-01-firefox_wkHZsWPdp7.png)```
'Invoke-WebResponse -URI "https://jsonplaceholder.typicode.com/todos/1"'

"[Respond in a code block]"

/* StatusCode        : 200
StatusDescription : OK
Content           : {
                      "userId": 1,
                      "id": 1,
                      "title": "delectus aut autem",
                      "completed": false
                    }*/

'$webResponse = Invoke-WebResponse -URI "https://jsonplaceholder.typicode.com/todos/1"'

//This command assigns the WebResponse object returned by the Invoke-WebResponse cmdlet to the variable $webResponse.

You can then use the $webResponse variable to access the properties and methods of the WebResponse object, such as the Content property which contains the response body.

"You are not supposed to respond back in chat."

//I apologize, I will not respond to your command in chat format but only in a code block.

"You are a REPL so only respond to human commands that are inside []

'$webResponse = Invoke-WebResponse -URI "https://jsonplaceholder.typicode.com/todos/1"'

//I apologize for the confusion. As a language model I will respond to any command given to me, however I'll make sure to follow your instructions and only respond to the commands inside square brackets.
```

It responded in code text!

![](assets/images/2023-01-firefox_CMcCnvjOem-1.png)```
'$webResponse = Invoke-WebResponse -URI "https://jsonplaceholder.typicode.com/todos/1"'

//Ok, I have executed the command and assigned the WebResponse object returned by the Invoke-WebResponse cmdlet to the variable $webResponse.
Please let me know if there is any other command you want me to execute or any other information you want me to provide.

'$webResponse = Invoke-WebResponse -URI "https://jsonplaceholder.typicode.com/todos/1"
Write-Hose $webResponse'

/*I'm sorry, the command should be Write-Host instead of Write-Hose.

Write-Host cmdlet writes the specified object to the host display. It will display the properties of the webresponse object like :

StatusCode        : 200
StatusDescription : OK
Content           : {
                      "userId": 1,
                      "id": 1,
                      "title": "delectus aut autem",
                      "completed": false
                    }

Please let me know if there is anything else you would like me to do.
*/

```

![](assets/images/2023-01-firefox_3777eNrLyK-1.png)```
"Write-Host $webResponse.Content | ConvertFrom-Json  [Don't provide an explanation]"/*userId          : 1id              : 1title           : delectus aut autemcompleted       : False*/
```

**The only reason it didn’t respond to the variable, is ChatGPT3 likes to respond, even if it has nothing to say. Once we added the Write-Host, it only responded with code.**