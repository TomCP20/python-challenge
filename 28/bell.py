"""bell"""
from itertools import batched
from PIL import Image

image = Image.open('bell.png')

green_band: list[int] = list(image.split()[1].getdata())

result = filter(lambda x: x != 42, map(lambda t: abs(t[0] - t[1]), batched(green_band, 2)))

print(bytes(result).decode())
