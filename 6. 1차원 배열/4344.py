trial = int(input())

strings = []
stcount = []
stscore = []

for i in range(trial):
    strings.append(input())
    
for j in strings:
    temp = list(map(int, j.split(" ")))
    stcount.append(int(temp[0]))
    del temp[0]
    stscore.append(temp)
    
for i in range(trial):
    cur = stscore[i]
    avg = sum(cur) / stcount[i]
    sup = list(filter(lambda x: x > avg, stscore[i]))
    percentage = round((len(sup) / stcount[i]) * 100, 3)
    print("%.3f" %(percentage),"%", sep="")