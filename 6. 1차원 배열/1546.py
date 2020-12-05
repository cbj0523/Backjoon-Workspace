trial = int(input())

numinput = input()

numinput = numinput.split(" ")

numinput = list(map(int, numinput))

afternum = []
maxscore = max(numinput)

for i in numinput:
    temp = (i / maxscore) * 100
    temp = round(temp, 2)
    afternum.append(temp)
    
print(sum(afternum) / trial)