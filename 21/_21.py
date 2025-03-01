"""21"""
import bz2
from zipfile import ZipFile
import zlib

with ZipFile('21.zip', 'r') as z:
    with z.open("readme.txt", pwd=bytes("redavni", "utf-8")) as f:
        print(f.read().decode("utf-8"))
    with z.open("package.pack", pwd=bytes("redavni", "utf-8")) as f:
        DATA: bytes = f.read()
        result: str = ""
        while True:
            if DATA.startswith(b'x\x9c'):
                DATA = zlib.decompress(DATA)
                result += " "
            elif DATA.startswith(b'BZh'):
                DATA = bz2.decompress(DATA)
                result += "#"
            elif DATA.endswith(b'\x9cx'):
                DATA = DATA[::-1]
                result += "\n"
            else:
                break
        print(DATA[::-1].decode("utf-8"))
        print(result)
