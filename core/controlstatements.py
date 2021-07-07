import random

for _ in range(50):
    data = random.randint(1, 500)
    if data < 300:
        print(data, end="\t")
