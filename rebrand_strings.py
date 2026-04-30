import os
import re

paths = [
    'd:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values/strings.xml',
    'd:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-vi/strings.xml',
    'd:/codes/ytmusic/ytmusic/core/media/media3/src/main/res/values/strings.xml'
]

# Add more paths if needed, but these are the main ones.
# Actually, let's just do all of them found by Get-ChildItem.

# I'll just use the list from the previous command output.
all_paths = [
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-ar/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-az/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-bg/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-ca/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-de/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-es/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-fa/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-fi/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-fr/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-hi/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-in/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-it/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-iw/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-ja/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-ko/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-nl/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-pl/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-pt/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-ru/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-th/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-tr/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-uk/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-vi/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-zh/strings.xml',
    'D:/codes/ytmusic/ytmusic/composeApp/src/commonMain/composeResources/values-zh-rTW/strings.xml',
    'D:/codes/ytmusic/ytmusic/core/media/media3/src/main/res/values/strings.xml'
]

for p in all_paths:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        c = c.replace('SimpMusic', 'Trider Music')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)

print("Rebranded all strings.xml files.")
