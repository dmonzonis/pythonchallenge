import re

with open("input.txt") as inp:
    mess = inp.read()

print(re.sub(r"[^a-zA-Z]", "", mess))
