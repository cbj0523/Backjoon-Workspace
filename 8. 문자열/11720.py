count = int(input())

chars = input()

result = 0

for i in list(map(int, chars)):
    result += i
    
print(result)