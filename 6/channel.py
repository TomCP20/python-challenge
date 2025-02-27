"""channel"""

import re
import zipfile

num: str = "90052"
out: str = ""
with zipfile.ZipFile("channel.zip") as z:
    while True:
        out += (z.getinfo(f"{num}.txt").comment.decode("utf-8"))
        path = zipfile.Path(z, f"{num}.txt")
        text = path.read_text(encoding="utf-8")
        match = re.fullmatch(r"Next nothing is (\d+)", text)
        if match:
            num = match.groups()[0]
        else:
            print("no match")
            print(num)
            print(text)
            break
print(out)
