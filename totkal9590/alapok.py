import random
# 1. feladat
keresztnev = input("Kérem a keresztneved: ")
vezeteknev = input("Kérem a vezeték neved: ")
teljes_nev = vezeteknev+" "+keresztnev
print(f"Üdvözöllek {teljes_nev}")

# 2. feladat
lista = list()
for i in range(0,10):
    lista.append(random.randint(1,10))

szam=int(input("Kérek egy egész számot 1 és 7 között: "))
if lista.count(szam) > 0:
    print("A szám a listában volt.")
else:
    print("A szám nincs a listában.")
    print(f"A lista: {lista}")
'''
# 3. feladat
with open('szamok.txt', 'r', encoding='utf-8') as fajl:
    fajl.write(int(szam))
'''
# 4. feladat
def addSzor():
    szam3=szam1+szam2
    eredmeny=szam3*2
    return eredmeny
szam1 = int(input("Kérek egy számot: "))
szam2 = int(input("Kérek egy másik számot: "))
print(f"Eredmény: {szam1},{szam2} -> {addSzor()}")

# 5.(1) feladat
'''
adatok = []
with open('snooker.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        adatok.append(sor.strip())

versenyzo = {}
versenyzok = []
for elem in adatok:
    versenyzo_adatai = elem.split()
    versenyzo['helyezes'] = versenyzo_adatai[0]
    versenyzo['nev'] = versenyzo_adatai[1]
    versenyzo['orszag'] = versenyzo_adatai[2]
    versenyzo['nyeremeny'] = int(versenyzo_adatai[3])

    versenyzok.append(versenyzo)
    versenyzo = {}

print(versenyzok) # out of range
'''