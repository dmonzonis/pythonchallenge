import re

with open("input.txt") as inp:
    mess = inp.read()

matches = re.findall(r"[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", mess)
print("".join(matches))
