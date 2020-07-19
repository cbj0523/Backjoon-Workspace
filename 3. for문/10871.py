N, X = map(int, input().split())

A = list(map(int, input().split()))

result = []

for element in A:
    if element < X:
        result.append(element)
        
for data in result:
    print(data, end=" ")