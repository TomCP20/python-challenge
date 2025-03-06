"""ambiguity"""
from collections import deque
import io
from zipfile import ZipFile

from PIL import Image, ImageFile


Vec = tuple[int, int]
Path = list[Vec]

def bfs(w: int, h: int, image: ImageFile.ImageFile):
    """bfs"""
    def neighbors(n: Vec):
        x, y = n
        white = (255, 255, 255, 255)
        if (x+1, y) not in visited and x+1 < w and image.getpixel((x+1, y)) != white:
            yield (x+1, y)
        if (x-1, y) not in visited and x-1 >= 0 and image.getpixel((x-1, y)) != white:
            yield (x-1, y)
        if (x, y+1) not in visited and y+1 < h and image.getpixel((x, y+1)) != white:
            yield (x, y+1)
        if (x, y-1) not in visited and y-1 >= 0 and image.getpixel((x, y-1)) != white:
            yield (x, y-1)

    q: deque[Path] = deque([[(w-1, 0)]])
    visited: set[Vec] = set()

    while q:
        path = q.popleft()
        node = path[-1]
        visited.add(node)

        if node[1] == h-1:
            return path

        for adj in neighbors(node):
            new_path = list(path)
            new_path.append(adj)
            q.append(new_path)
    assert False

def main():
    """main"""
    image = Image.open("maze.png")

    w, h = image.size
    path = bfs(w, h, image)
    vals: list[int] = []
    for node in path:
        p = image.getpixel(node)
        assert isinstance(p, tuple)
        r, _, _, _ = p
        vals.append(r)
    data = io.BytesIO(bytes(vals[::2]))
    with ZipFile(data) as z:
        print(z.filelist)
        with z.open("maze.jpg") as f:
            Image.open(f).show()
        with z.open("mybroken.zip") as f:
            with open("mybroken.zip", "wb") as o:
                o.write(f.read())

main()
