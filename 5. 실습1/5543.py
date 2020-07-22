burger = []
drink = []
total = 0

for i in range(3):
    burgerinput = int(input())
    burger.append(burgerinput)

for j in range(2):
    drinkinput = int(input())
    drink.append(drinkinput)
    
setburger = min(burger)
setdrink = min(drink)

total = setburger + setdrink - 50

print(total)