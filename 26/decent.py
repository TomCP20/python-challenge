"""decent"""
import hashlib
import io
from itertools import product
from zipfile import ZipFile
from PIL import Image

with open("mybroken.zip", "rb") as f:
    data = f.read()
new_data: bytes | None = None
for i, j in product(range(len(data)), range(256)):
    new_data = data[:i] + bytes([j]) + data[i + 1:]
    if hashlib.md5(new_data).hexdigest() == "bbb8b499a0eef99b52c7f13f4e78c24b":
        break
if new_data:
    with ZipFile(io.BytesIO(new_data)) as z:
        with z.open("mybroken.gif") as f:
            Image.open(f).show()
