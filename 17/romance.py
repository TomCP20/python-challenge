"""romance"""
import re
from urllib.parse import unquote, unquote_to_bytes
from bz2 import decompress
import xmlrpc.client

import requests

response = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php', timeout=10)
print(unquote(response.cookies.get_dict()["info"]))

LINKED_LIST_URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
num: str = "12345"
data: str = ""
while True:
    response = requests.get(LINKED_LIST_URL+num, timeout=10)
    if response.status_code == 200:
        data += response.cookies.get_dict()["info"]
        match = re.search(r"and the next busynothing is (\d+)", response.text)
        if match:
            num = match.groups()[0]
        else:
            break
    else:
        print(f"Could not find url: {LINKED_LIST_URL+num}")
        break
print(decompress(unquote_to_bytes(data)).decode("utf-8"))

class MyTransport(xmlrpc.client.Transport):
    """custom transport class"""
    accept_gzip_encoding = False

PHONEBOOK_URL = "http://www.pythonchallenge.com/pc/phonebook.php"
phonebook = xmlrpc.client.ServerProxy(PHONEBOOK_URL, transport=MyTransport())
print(phonebook.phone("Leopold"))

VIOLIN_URL = "http://www.pythonchallenge.com/pc/stuff/violin.php"

cookies = {"info": "the flowers are on their way"}

response = requests.get(VIOLIN_URL, cookies=cookies, timeout=10)
print(response.text)
