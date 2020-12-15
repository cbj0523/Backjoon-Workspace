word = input()

result = []

for i in range(97, 123):
    try: 
        j = word.index(chr(i))
        result.append(j)
    except:
        result.append(-1)
        
for i in result:
    print(i, end=" ")