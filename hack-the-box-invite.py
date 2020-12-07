#!/usr/bin/env python3

import requests
import json
import re
import base64
import sys

url = "https://www.hackthebox.eu/api/invite/generate"
headers = {
"Host": "www.hackthebox.eu",
"User-Agent": "curl/7.64.1",
"Accept" : "*/*"
}

#curl -X POST https://www.hackthebox.eu/api/invite/generate

response = requests.post(url, data="", headers=headers)
jsonResponse = response.json()
code = jsonResponse["data"]["code"]
decodedCode = base64.b64decode(code)
print(decodedCode)
