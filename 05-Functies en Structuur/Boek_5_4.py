import random

getallen = []
for i in range(1, 11):
    getallen.append(random.randint(1, 10))

print(getallen)
random.shuffle(getallen)
print(getallen)
