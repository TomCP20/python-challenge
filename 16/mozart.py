"""mozart"""
from PIL import Image, ImageChops

image = Image.open("mozart.gif")

for y in range(image.size[1]):
    box = 0, y, image.size[0], y + 1
    row = image.crop(box)
    bytedata = row.tobytes()
    i = bytedata.index(195)
    row = ImageChops.offset(row, -i)
    image.paste(row, box)

image.show()
