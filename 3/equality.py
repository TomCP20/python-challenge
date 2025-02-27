"""equality"""
import re

with open("input.txt", encoding="utf-8") as f:
    TEXT = f.read()
matches = re.findall(r"[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", TEXT)
print("".join(matches))
