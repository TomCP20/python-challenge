"""oxygen"""
from PIL import Image

image = Image.open("oxygen.png")
w, h = image.size
px = image.load()
out: str = ""
if px:
    for r, g, b, _ in [px[x, h//2] for x in range(0, w, 7)]:
        if r == g == b:
            out += chr(r)
print(out)
start = out.index("[")
end = out.index("]")
print("".join(map(lambda x: chr(int(x)), out[start+1:end].split(", "))))
