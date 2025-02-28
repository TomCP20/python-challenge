"""evil"""
import io
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

with open("evil2.gfx", "rb") as f:
    data = f.read()
for i in range(5):
    image = Image.open(io.BytesIO(data[i::5]))
    image.show()
