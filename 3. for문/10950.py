count = int(input())

dic = []

for i in range(count):
    a, b = input().split()
    a = int(a)
    b = int(b)
    
    dic.append(a + b)
    
    
for j in dic:
    print(j)