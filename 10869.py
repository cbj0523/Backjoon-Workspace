numbers = input("").split(" ")

numbers = list(map(int, numbers))

print("{}".format(numbers[0] + numbers[1]))
print("{}".format(numbers[0] - numbers[1]))
print("{}".format(numbers[0] * numbers[1]))
print("{}".format(int(numbers[0] / numbers[1])))
print("{}".format(numbers[0] % numbers[1]))
