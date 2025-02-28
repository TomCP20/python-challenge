"""cow"""

from itertools import groupby

def step(val: str):
    """produces the next value in the sequence"""
    nextval = ""
    for k, g in groupby(val):
        nextval += str(len(list(g))) + k
    return nextval


n: str = "1"
for i in range(30):
    n = step(n)
print(len(n))
