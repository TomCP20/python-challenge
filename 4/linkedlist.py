"""linkedlist"""
import re
import requests

URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num: str = "12345"
response: requests.Response | None = None
for i in range(400):
    print(i, num)
    response = requests.get(URL+num, timeout=10)
    if response.status_code == 200:
        match = re.search(r"and the next nothing is (\d+)", response.text)
        if match:
            num = match.groups()[0]
        elif response.text == "Yes. Divide by two and keep going.":
            num: str = str(int(int(num)/2))
        else:
            print("no match")
            break
    else:
        print(f"Could not find url: {URL+num}")
        break
if response:
    print(response.text)
