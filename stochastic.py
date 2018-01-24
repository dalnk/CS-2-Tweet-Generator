import random

with open('fish.txt', 'r+') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]
    print(random.choice(lines))
