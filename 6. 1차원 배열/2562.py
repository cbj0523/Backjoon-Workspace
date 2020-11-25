number = []

for i in range(9):
    number.append(int(input()))

print(max(number))
print(int(number.index(max(number)) + 1))