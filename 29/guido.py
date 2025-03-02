"""guido"""
import bz2

with open("input.txt", encoding="utf-8") as f:
    print(bz2.decompress(bytes(map(len, f.read().splitlines()))).decode())
