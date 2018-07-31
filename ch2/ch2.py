rot2 = str.maketrans("abcdefghijklmnopqrstuvwxyz",
                  "cdefghijklmnopqrstuvwxyzab")

with open("input.txt") as inp:
    orig = inp.read()

print(orig.translate(rot2))
print("map".translate(rot2))

