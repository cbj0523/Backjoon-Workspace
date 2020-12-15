count = int(input())

result = []

group_word = 0

for i in range(count):
    result.append(input())
    
for word in result:
    group_or_not = 1
    for j in range(0, len(word) - 1):
        if word[j] != word[j+1]:
            if word[j+1:].count(word[j]) > 0:
                group_or_not = 0
    if group_or_not == 1:
        group_word += 1

print(group_word)