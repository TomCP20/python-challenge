"""balloons"""
import gzip
import difflib
import io
from PIL import Image

with gzip.open('deltas.gz') as data:
    col1, col2 = [], []
    for line in data:
        col1.append(line[:53].decode()+"\n")
        col2.append(line[56:].decode())
    compare = difflib.Differ().compare(col1, col2)
    f: bytes = b""
    f1: bytes = b""
    f2: bytes = b""
    for line in compare:
        bs = bytes([int(o, 16) for o in line[2:].strip().split(" ") if o])
        if line[0] == '+':
            f1 += bs
        elif line[0] == '-':
            f2 += bs
        else:
            f += bs
    Image.open(io.BytesIO((f))).show()
    Image.open(io.BytesIO((f1))).show()
    Image.open(io.BytesIO((f2))).show()
