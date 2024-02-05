
v = {}
print(type(v))
v = []
print(type(v))
v = ()
print(type(v))
print("***************")

v = set()
v.add(1)
v.add(2)
v.add(1) # nem írja mégegyszer ezt a számot
print(v)
v = list()
v.append(1)
v.append(2)
v.append(1) # ez kiírja mégegyszer a számot
print(v)

v = tuple()
print(type(v))
v = dict()
print(type(v))

# ------------------------

szotar = {"nev":"Pista", "kor":14}
print(szotar)
print(szotar["nev"])

sor = "Amet ipsum nulla magna cupidatat mollit excepteur consectetur aliquip qui adipisicing."
lista = sor.replace(".","").split(" ") # a replace kiveszi a pontot egy üres dologra, a split meg mindegyik szót külön veszi egy listában
#print(lista)

szavak = dict()
kulcs = 1
for szo in lista:
    #print(szo)
    szavak.update({kulcs:szo})
    kulcs += 1
print(szavak)

for x in szavak:
    print(x,end=", ") # kiírja a kulcs listázását
print()

for x in szavak:
    print(x,szavak[x]) # kiírja a kulcsot és a szót
print()

for kulcs in szavak:
    print(kulcs,szavak[kulcs]) # ugyanaz mint a fölötti
print()


for x in szotar.keys(): # kiírja a kulcsot csak
    print(x,end=", ")
print()

for x in szotar.values(): # kiírja az elemet csak
    print(x,end=", ")
print()

for k,e in szotar.items(): # kiírja az elemet és az elemet
    print("kulcs:",k,"érték:",e)



szemelyek = list()
szemely = {"név":"Pista","kor":14,"nem":"fiú"}
szemelyek.append(szemely)

szemely = {"név":"Ági","kor":13,"nem":"lány"}
szemelyek.append(szemely)

szemely = {"név":"Bodri","kor":15,"nem":"fiú"}
szemelyek.append(szemely)

szemely = {"név":"Zalán","kor":14,"nem":"fiú"}
szemelyek.append(szemely)

print(szemelyek)

for szem in szemelyek:
    print(szem["név"]) # csak a neveket írja ki

for szem in szemelyek:
    if szem["nem"] == "fiú":
        print(szem["kor"]) # csak a FIÚKNAK a korát írja ki

osszeg = 0
db = 0
for szem in szemelyek:
    osszeg += szem["kor"]
    db += 1
print(osszeg/db) # kor átlag számolása
# vagy
#print(osszeg/len(szemelyek)) [és a db változó nem kell] 

osszeg = 0
db = 0
for szem in szemelyek:
    if szem["nem"] == "fiú":
        osszeg += szem["kor"]
        db += 1
print(osszeg/db)

for szem in szemelyek:
    szem["kor"] += 1
