import random

gondolt = random.randint(1,100)

tipp = 0
while tipp < 1 or tipp > 100:
    tipp = int(input("Kérek egy 1 és 100 közé eső számot: "))
    
print(tipp)
