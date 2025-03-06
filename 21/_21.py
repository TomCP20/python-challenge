"""21"""
import bz2
from zipfile import ZipFile
import zlib

with ZipFile('21.zip', 'r') as z:
    with z.open("readme.txt", pwd=bytes("redavni", "utf-8")) as f:
        print(f.read().decode("utf-8"))
    with z.open("package.pack", pwd=bytes("redavni", "utf-8")) as f:
        data: bytes = f.read()
        result: str = ""
        while True:
            if data.startswith(b'x\x9c'):
                data = zlib.decompress(data)
                result += " "
            elif data.startswith(b'BZh'):
                data: bytes = bz2.decompress(data)
                result += "#"
            elif data.endswith(b'\x9cx'):
                data = data[::-1]
                result += "\n"
            else:
                break
        print(data[::-1].decode("utf-8"))
        print(result)
