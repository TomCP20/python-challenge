"""oxygen"""
from PIL import Image

image = Image.open("oxygen.png")
w, h = image.size
#px = image.getpixel()
out: str = ""
for x in range(0, w, 7):
    p = image.getpixel((x, h//2))
    assert isinstance(p, tuple)
    r, g, b, _ = p
    if r == g == b:
        out += chr(r)
print(out)
start = out.index("[")
end = out.index("]")
print("".join(map(lambda x: chr(int(x)), out[start+1:end].split(", "))))
