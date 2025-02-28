"""good"""

from itertools import batched
from PIL import Image


with open("input.txt", encoding="utf-8") as f:
    both = list(batched(map(int, "".join(f.read().splitlines()).split(",")), 2))
    image = Image.new(mode="RGB", size=(450, 450))
    for x, y in both:
        image.putpixel((x, y), (255, 255, 255, 255))
    image.show()

