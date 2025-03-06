"""beer"""
import math
from PIL import Image

image = Image.open('beer2.png')

data: list[int] = list(image.getdata()) # type: ignore


letters: list[Image.Image] = []
for _ in range(33):
    max_value = max(data)
    data = [x for x in data if x < max_value - 1]
    l = int(math.sqrt(len(data)))
    letter = Image.new('L', (l, l))
    letter.putdata(data) # type: ignore
    letters.append(letter)

w = sum(letter.size[0] for letter in letters)
h = letters[0].size[1]

result = Image.new("L", (w, h))

offset: int = 0
for letter in letters:
    result.paste(letter, (offset, 0))
    offset += letter.size[0]
result.show()
