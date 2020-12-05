trial = int(input())

result = []

ocount = []

for i in range(trial):
    result.append(input())
    
for j in result:
    temp = list(j)
    oscore = 0
    pscore = 1
    for l in temp:
        if l == "O":
           oscore += pscore
           pscore += 1
        if l == "X":
            pscore = 1
        
    print(oscore)
    
