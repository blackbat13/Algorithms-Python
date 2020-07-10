import random


def rand(probability: int) -> bool:
    x = random.randint(1, 100)
    return x <= probability


probability = 50
count = 0
n = 100000
for i in range(0, n):
    if rand(probability):
        count += 1

print(f"Probability: {probability}%, {n} tests, result: {count}/{n} ~= {100*count/n}%")
