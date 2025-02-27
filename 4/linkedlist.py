"""linkedlist"""
import re
import requests

URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
NUM = "12345"
for i in range(400):
    print(i, NUM)
    response = requests.get(URL+NUM, timeout=10)
    if response.status_code == 200:
        match = re.search(r"and the next nothing is (\d+)", response.text)
        if match:
            NUM = match.groups()[0]
        elif response.text == "Yes. Divide by two and keep going.":
            NUM = str(int(int(NUM)/2))
        else:
            print("no match")
            break
    else:
        print(f"Could not find url: {URL+NUM}")
        break
print(response.text)
