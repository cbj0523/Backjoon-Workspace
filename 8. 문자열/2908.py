numbers = input().split()

for i in range(0, 2):
    numbers[i] = int("".join(list(reversed(numbers[i]))))
    
print(max(numbers))