"""5808"""
from PIL import Image

image = Image.open("cave.jpg")
(w, h) = image.size

even = Image.new('RGB', (w//2, h//2))

for x in range(w):
    for y in range(h):
        if (x+y)%2 == 0:
            p = image.getpixel((x,y))
            assert p
            even.putpixel((x//2,y//2), p)
even.show()
