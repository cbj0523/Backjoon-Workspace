N = int(input())

result = []

for n in range(1, N+1):
    tr = False
    nlist = list(str(n))
    if len(nlist) <= 1:
        tr = True
    else:
        d = int(nlist[0]) - int(nlist[1])
        for i in range(0, (len(nlist) - 1)):
            if d == int(nlist[i]) - int(nlist[i+1]):
                tr = True
            else:
                tr = False
    if tr:
        result.append(n)
        
print(len(result))