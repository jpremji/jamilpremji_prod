---
id: 262
title: 'Integrating ChatGPT3 with PowerShell'
date: '2023-01-05T01:54:27-04:00'
author: jamilpremji
layout: post
guid: 'https://jamilpremji.com:443/?p=262'
permalink: /:year-:month-:day-:title
burst_total_pageviews_count:
    - '121'
image: /wp-content/uploads/2023/01/pngwing.com_.png
categories:
    - PowerShell
---

PowerShell is a powerful task automation and configuration management framework from Microsoft, consisting of a command-line shell and associated scripting language. ChatGPT is a large language model developed by OpenAI that can generate human-like text. In this article, we will show you how to use ChatGPT in a PowerShell script to request a prompt and speak it out using the built-in SpeechSynthesizer class.

Prerequisites:

- [ChatGPT API key](https://beta.openai.com/account/api-keys). You can obtain a free API key by signing up for an OpenAI account at .
- PowerShell 5.0 or later. You can check the version of PowerShell you have installed by running the command `$PSVersionTable.PSVersion` in a PowerShell window.

```powershell
The following line needs to be replaced with your key in the script below:

$apiKey = 'REPLACE-THIS-WITH-YOUR-KEY'  #The key starts with SK-

```

```powershell
param (
  [string] $Prompt
)

function Query-OpenAIAPI {
  param (
    [Parameter(Mandatory)]
    [string] $apiKey,

    [Parameter(Mandatory)]
    [string] $prompt,

    [string] $model = "text-davinci-003",
    [int] $responses = 1,
    [int] $length = 2048
  )

  $body = @{
    model = $model
    prompt = $prompt
    n = $responses
    max_tokens = $length
  } | ConvertTo-Json
  
  $response = Invoke-RestMethod -Uri "https://api.openai.com/v1/completions" -Method "POST" -Body $body -Headers @{ "Authorization" = "Bearer $apiKey" } -ContentType "application/json"
  return $response[0].choices[0].text
} 

Add-Type -AssemblyName System.Speech
$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer
$apiKey = 'REPLACE-THIS-WITH-YOUR-KEY'  #The key starts with SK-




if (!$prompt) {
  $prompt = Read-Host "Enter a prompt:"
}
$speak.Speak("Prompt:" + $Prompt)

$result = Query-OpenAIAPI  -prompt $prompt -apiKey $apiKey
$speak.Speak("Result:" + $result)
```

This script appears to define a function called `Query-OpenAIAPI` that sends a request to the OpenAI API and returns the response.

The `Query-OpenAIAPI` function has several parameters:

- `$apiKey`: This is the API key required to authenticate the request.
- `$prompt`: This is the text prompt that is sent to the OpenAI API.
- `$model`: This is the name of the model to use for generating text. The default value is “text-davinci-003”.
- `$responses`: This is the number of responses to generate. The default value is 1.
- `$length`: This is the maximum number of tokens (i.e., words and punctuation) in the generated responses. The default value is 2048.

The function sends a `POST` request to the OpenAI API with the specified prompt, model, and other parameters. [The API key](https://beta.openai.com/account/api-keys) is included in the request headers. The response is returned as a JSON object, and the `text` field of the first `choice` in the response is returned.

Below the function definition, the script adds a reference to the `System.Speech` assembly, creates a new `SpeechSynthesizer` object, and stores the object in a variable called `$speak`.

The script then sets a default value for the `$prompt` parameter and displays it to the user. If the user doesn’t provide a value for `$prompt`, they are prompted to enter one.

Next, the script calls the `Query-OpenAIAPI` function, passing in `$prompt` and `$apiKey` as arguments. The result is stored in the `$result` variable.

Finally, the script uses the `Speak` method of the `$speak` object to speak the prompt and result text aloud.