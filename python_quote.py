import random

quotes = ("It's just a flesh wound.", "This is an EX-PARROT")

rand_index = random.randint(0, len(quotes) - 1)
print(quotes[rand_index])
