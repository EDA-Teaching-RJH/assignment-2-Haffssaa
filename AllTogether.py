### Part Four -- your code goes here. 
import random

numbers = []

for x in range(10):
    numbers.append(random.randint(1, 100))
print("Here is the original list:", numbers)

x = 0
while x < len(numbers):
    if numbers[x] % 2 == 0:
        numbers.pop(x)
    else:
        x += 1

print("Remaining odd numbers:", numbers)
