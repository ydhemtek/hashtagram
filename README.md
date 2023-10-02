
# Hashtagram

### Instagram Keyword Search and RSS News Tool

This script allows you to retrieve Instagram posts based on specific keywords or hashtags. Additionally, it can extract relevant hashtags from specified RSS news feeds.
### Features

Search for Instagram posts based on keywords or hashtags.
Monitor multiple keywords using RSS feeds and create hashtag lists from the news.

- Coded with Python 3
- Built-in modules use Tor proxy
- Uses undetected-chromedriver


### Installation

```
pip install -r requirements.txt
```

### launch

```
python3 Hashtagram
```

### keywords

in the ```keywords.txt``` file you must place the keywords in this way

```
Novorossiya
Donbass
Slavyansk
Lugansk
DNR
LNR
RussieUnie
СлаваРоссии
Путин
МирныйЗахват
РусскаяМир
Сепаратизм
ВосточнаяУкраина
МирВДонбассе
Сирия
РоссийскаяАрмия
Донецк
Луганск
МирВУкраине
Православие
donbas
donetsk
```
this keywords file example is for the Russo-Ukrainian War

### why this tool ?

this tool can be useful for osint or geoint

### Error Cases/Warnings
#### Recurring Error Types
```
selenium.common.exceptions.WebDriverException: Message: unknown error: cannot connect to chrome at 127.0.0.1:46973
from session not created: This version of ChromeDriver only supports Chrome version 112
Current browser version is 111.0.5563.146
Stacktrace:
#0 0x55bf0fd28fe3 <unknown>
#1 0x55bf0fa67d36 <unknown>
#2 0x55bf0fa9548c <unknown>
#3 0x55bf0fa8c352 <unknown>
#4 0x55bf0faceaf7 <unknown>
#5 0x55bf0face11f <unknown>
#6 0x55bf0fac5693 <unknown>
#7 0x55bf0fa9803a <unknown>
#8 0x55bf0fa9917e <unknown>
#9 0x55bf0fceadbd <unknown>
#10 0x55bf0fceec6c <unknown>
#11 0x55bf0fcf84b0 <unknown>
#12 0x55bf0fcefd63 <unknown>
#13 0x55bf0fcc2c35 <unknown>
#14 0x55bf0fd13138 <unknown>
#15 0x55bf0fd132c7 <unknown>
#16 0x55bf0fd21093 <unknown>
#17 0x7f8f5da8cded start_thread
```

## ⚠️ Make sure you always have the latest version of Chrome or Chromium compatible with the latest version of selenium undetectable, currently chrome 114. ⚠️

search on the internet for a version of chrome requested by selenium. Here {Recurring Error Types} "This version of ChromeDriver only supports Chrome version 112"

## ⚠️ Make sure you installed Tor ⚠️

for the installations go to the official Tor page

## ⚠️ use with caution... this tool is an educational tool ⚠️
