"""idiot"""
import requests

def get_response(num: int):
    """get the response from range num"""
    url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
    return requests.get(url, auth=("butter", "fly"), timeout=10, headers={"Range":f"bytes={num}-"})

print(get_response(0).headers["Content-Range"])
print(get_response(30203).text.strip())
print(get_response(30237).text.strip())
print(get_response(30284).text.strip())
print(get_response(30295).text.strip())
print(get_response(30313).text.strip())
print(get_response(2123456790).text.strip()[::-1])
print(get_response(2123456743).text.strip())
with open("21.zip", "wb") as f:
    f.write(get_response(1152983631).content)
