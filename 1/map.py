"""map"""

TEXT = input("Enter your text:\n")
mytable = {i+ord("a"): (i+2)%26+ord("a") for i in range(26)}
print(TEXT.translate(mytable))
