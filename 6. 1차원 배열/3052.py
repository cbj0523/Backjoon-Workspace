number = []
temp = []

for i in range(10):
    number.append(int(input()))

for i in number:
    if i % 42 not in temp:
        temp.append(i % 42)
    
print(len(temp))