"""disproportional"""

import xmlrpc.client

class MyTransport(xmlrpc.client.Transport):
    """custom transport class"""
    accept_gzip_encoding = False

URL = "http://www.pythonchallenge.com/pc/phonebook.php"
phonebook = xmlrpc.client.ServerProxy(URL, transport=MyTransport())
print(phonebook.system.listMethods())
print(phonebook.system.methodHelp("phone"))
print(phonebook.system.methodSignature("phone"))
print(phonebook.phone("Bert"))
