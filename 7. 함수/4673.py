number = []

for i in range(1, 10001):
    number.append(i)

def d(n):
    i = list(str(n))
    l = 0
    for j in i:
        l += int(j)
    return n + l

for i in range(1, 10001):
    try:
        number.remove(d(i))        
    except:
        pass
        
for i in number:
    print(i)