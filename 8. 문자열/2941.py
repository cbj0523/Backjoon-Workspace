string = input()

chars = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in chars:
    string = string.replace(i, "0")

print(len(string))