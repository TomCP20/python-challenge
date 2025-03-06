"""copper"""
from PIL import Image, ImageDraw

Vec = tuple[int, int]

def sub(a: Vec, b: Vec) -> Vec:
    """returns the difference between 2 vecs"""
    return (b[0]-a[0], b[1]-a[1])

image = Image.open("white.gif")
output = Image.new("RGB", (500, 200))
draw = ImageDraw.Draw(output)
x, y = 0, 100

for frame in range(image.n_frames): # type: ignore
    image.seek(frame)

    box = image.getbbox()
    assert box
    l, u, _, _ = box

    dx = l - 100
    dy = u - 100

    if dx == dy == 0:
        x +=50
        y: int = 100
    else:
        x += dx
        y += dy
    draw.point([x, y])

output.show()
