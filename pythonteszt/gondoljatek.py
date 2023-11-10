import random
# random.seed(0)
gondolt = random.randint(1,100)

talalt = False
tippSzam = 0
while not talalt:
    egesz = 0
    while egesz < 1 or egesz > 100:
        egesz = int(input("Kérek egy 1 és 100 közé eső számot: "))
    tippSzam += 1
    '''
    if gondolt < egesz:
        print("Nagyobb szám")
    if gondolt > egesz:
        print("Kisebb szám")
    if gondolt == egesz:
        print("Talált")
        talalt = True
    '''
    if gondolt < egesz:
        print("Tipped nagyobb szám")
    elif gondolt > egesz:
        print("Tipped kisebb szám")
    else:
        print(tippSzam,"lépésben talált")
        talalt = True
