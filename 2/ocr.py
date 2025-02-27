"""ocr"""
with open("input.txt", encoding="utf-8") as f:
    TEXT = f.read()
for c in TEXT:
    if c.isalpha():
        print(c, end="")
