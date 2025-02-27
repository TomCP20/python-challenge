"""peak"""
import pickle

with open('banner.p', 'rb') as f:
    file = pickle.load(f)
for l in file:
    for a, b in l:
        print(a*b, end="")
    print()
