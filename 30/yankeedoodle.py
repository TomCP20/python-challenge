"""yankeedoodle!"""
from math import sqrt
from itertools import batched
import re

from PIL import Image

def get_factors(n: int):
    """returns factors of n"""
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return i, n//i
    return 1, n

with open("yankeedoodle.csv", encoding="utf-8") as csv:
    data = list(map(float, re.split(", |,\n", csv.read())))
    length = len(data)
    w, h = get_factors(length)
    image = Image.new("F", (w, h))
    image.putdata(data, 256)
    image.transpose(Image.Transpose.FLIP_LEFT_RIGHT).transpose(Image.Transpose.ROTATE_90).show()

    print(bytes([int(f"{a:.6f}"[5] + f"{b:.6f}"[5] + f"{c:.6f}"[6]) for a, b, c in batched(data[:-2], 3)]).decode())
