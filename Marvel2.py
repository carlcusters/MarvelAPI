# #!/usr/bin/python
# -*- coding: utf-8 -*-
#imports
import time
import hashlib
import urllib.parse
import urllib.request
import requests
import json
from tabulate import tabulate
import textwrap
# Variables
pub_key = 'Geef hier uw public key'
priv_key = 'Geef hier uw private key'
q = {}
q['ts'] = str(time.time())
q['apikey'] = pub_key
privateKey = priv_key
q['hash'] = hashlib.md5(
    bytes(q['ts'] + privateKey + q['apikey'], 'utf-8')).hexdigest()
# Parsing
params = urllib.parse.urlencode(q)
url = 'https://gateway.marvel.com:443/v1/public/characters?' + params
# Output
while True:
    user = input("Geef een karakter: ")
    if user == "quit" or user == "q":
        break
    try:
        d = requests.get(url).json()
        a = d["data"]["results"]
        for char in a:
            if user in char["name"]:
                c = char
        table = [["name: ", c["name"]], ["Desciprion: ",
                                         textwrap.shorten(c["description"], width=180, placeholder="...")], ["Hoeveelheid Comics: ", str(c["comics"]["available"])]]
        print(tabulate(table, tablefmt="plain"))
    except:
        print("Character bestaad niet. Probeer opnieuw")