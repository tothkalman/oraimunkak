# legkisebb szám
def kicsi(lista):
    k = lista[0]
    for e in lista:
        if e < k:
            k = e
    return k

print(kicsi([3,1,6,4]))

# legnagyobb szám
def nagy(lista):
    n = lista[0]
    for e in lista:
        if e > n:
            n = e
    return n

print(nagy([3,1,6,4]))

# számok kérése és kiírása
szamok = list()
ismet = True
while ismet:
    sz=input("Kérek egy számot: ")
    if sz == "":
        ismet = False
    else:
        szamok.append(int(sz))

print(szamok)

# hárommal oszthatók
def harommal(lista):
    db = 0
    for x in lista:
        if x % 3 == 0:
            db+1

print(harommal([2,3,4,5,6]))
