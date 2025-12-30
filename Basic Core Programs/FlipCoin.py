import random
flip = int(input("Number of time to flip coins:\n"))

if flip<=0:
    print("flips must be in positive")
else: 
    heads = 0
    tails = 0

for _ in range(flip):
    if random.random() < 0.5:
        tails = tails+1
    else:
        heads = heads+1
        
head_percent = (heads / flip) * 100
tails_percent = (tails / flip) * 100

print(f"Heads: {head_percent:.2f}")
print(f"Tails: {tails_percent:.2f}")
    