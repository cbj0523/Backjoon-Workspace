count = int(input())

repeat = []
rstring = []

for i in range(count):
    l = input()
    repeat = int(l.split(" ")[0])
    string = list(l.split(" ")[1])
    
    result = ""
    
    for j in string:
        result += j * repeat
    
    rstring.append(result)
    
for j in rstring:
    print(j)