string = input().upper()

result = [];

for ords in range(65, 91):
    result.append(string.count(chr(ords)))
    
if result.count(max(result)) >= 2:
    print("?")
else:
    print(chr(65 + result.index(max(result))))