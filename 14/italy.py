"""italy"""
from PIL import Image

image = Image.open("wire.png")
out = Image.new('RGB', (100, 100))

delta = [(1,0),(0,1),(-1,0),(0,-1)]

x,y,i = -1,0,0
d: int = 200
while d/2>0:
    for v in delta:
        steps: int = d // 2
        for s in range(steps):
            x, y = x + v[0], y + v[1]
            pixel = image.getpixel((i,0))
            assert pixel
            out.putpixel((x, y), pixel)
            i += 1
        d -= 1
out.show()
