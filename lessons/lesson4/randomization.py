# generating random numbers
import random

random_number = random.randint(1, 10)
print(random_number)

random_float = random.uniform(1, 10)
print(random_float)

coin_flip = random.randint(0,1)

if coin_flip == 0: 
    print("Heads")
else: 
    print("Tails")