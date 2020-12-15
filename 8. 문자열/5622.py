def retNum(char):
    char = char.upper()
    if char == "A" or char == "B" or char == "C":
        return 3
    if char == "D" or char == "E" or char == "F":
        return 4
    if char == "G" or char == "H" or char == "I":
        return 5
    if char == "J" or char == "K" or char == "L":
        return 6
    if char == "M" or char == "N" or char == "O":
        return 7
    if char == "P" or char == "Q" or char == "R" or char == "S":
        return 8
    if char == "T" or char == "U" or char == "V":
        return 9
    if char == "W" or char == "X" or char == "Y" or char == "Z":
        return 10
    
string = input()
sec = 0
for i in list(string):
    sec += retNum(i)
    
print(sec)