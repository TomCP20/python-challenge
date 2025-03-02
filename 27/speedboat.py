"""speedboat"""
import keyword
import bz2

from PIL import Image

image = Image.open("zigzag.gif")

palette = image.getpalette()
assert palette
palette = palette[::3]

table = bytes.maketrans(bytes(list(range(256))), bytes(palette))

raw = image.tobytes()

trans = raw.translate(table)

zipped = list(zip(raw[1:], trans[:-1]))

out = Image.new("RGB", image.size)
colours = [(255, 255, 255)] * len(raw)
for i, p in enumerate(zipped):
    if p[0] != p[1]:
        colours[i] = (0, 0, 0)
out.putdata(colours)
out.show()

s = [t[0] for t in zipped if t[0] != t[1]]
text: bytes = bz2.decompress(bytes(s))

print(set(w for w in text.split() if not keyword.iskeyword(w.decode())))
