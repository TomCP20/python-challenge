"""granpa"""
from operator import sub

from PIL import Image

image = Image.open("mandelbrot.gif")

LEFT = 0.34
BOTTOM = 0.57
WIDTH = 0.036
HEIGHT = 0.027
MAX_ITERATIONS = 128

w, h = image.size

xstep = WIDTH / w
ystep = HEIGHT/ h

mandelbrot = image.copy()
result = []
for y in range(h - 1, -1, -1):
    for x in range(w):
        c = complex(LEFT + x * xstep, BOTTOM + y * ystep)
        z: complex = 0 + 0j
        for i in range(MAX_ITERATIONS):
            z = z * z + c
            if abs(z) > 2:
                break
        result.append(i)
mandelbrot.putdata(result)

diff = filter(None, map(sub, image.getdata(), mandelbrot.getdata()))

out = Image.new("1", (23, 73))
out.putdata([i < 16 for i in diff])
out.resize((230,730)).show()
