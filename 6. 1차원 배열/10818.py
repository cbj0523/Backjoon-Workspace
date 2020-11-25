count = int(input())

numbers = input().split(" ")
numbers = list(map(int, numbers))

maxnum = max(numbers)
minnum = min(numbers)

print(minnum, maxnum)