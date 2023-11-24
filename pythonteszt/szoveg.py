#mondat = input("Kérek egy mondatot: ")
mondat = "Ez egy teszt mondat ide írtam, hogy nem!!"
print(len(mondat)) # hány betű van a mondatban (space is beleszámít)

db = 0 # ez mindig kell

# kiírja mennyi E betű van
for c in mondat:
    #print(c)
    if c == 'e' or c == 'E':
        db +=1
print(db,"darab E betű van")
# vagy
for c in mondat.lower():
    if c == 'e':
        db +=1
print(db,"darab E betű van")

# hány magánhangzó van a mondatban
maganhangzok = ('a','á','e','é','i','í','o','ó','ö','ő','u','ú','ü','ű')
magan = set()
print(type(magan))
for c in mondat.lower():
    for m in maganhangzok:
        if c == m:
            db +=1
            magan.add(c)
print(db,"magánhangzó van a mondatban")
print(len(magan),"darab különböző magánhangzó volt")


mondat2="Vettem egy kiló almát, almaszószt készítek belőle."
print(mondat2.replace("alma","körte")) # kicserél egy adott szót más szóra

mondat2=mondat2.replace("e","a")
print(mondat2)

mondat2=mondat2.replace("e","a",2) # csak kettőt cserél
print(mondat2)

#mondat2=mondat2.replace("e","a",2,3) HIBÁS
#print(mondat2)

print(mondat2.split(" ")) # elválaszt
print(mondat2.split(","))
print(mondat2.split("al"))


print(mondat2.count("e")) # megszámolja mennyi van belőle egy adott szövegnek


print(mondat2.encode("utf-8"))
print(mondat2.encode("latin2"))
print(mondat2.encode("utf-16"))
print(mondat2.encode("utf-32"))
# 2 a 16-dikon bit = 65535


#mondat2.format("","")


print(mondat2.isdecimal())
print("12".isnumeric())

#szam = int(input("Kérek egy egész számot: "))
ismeteld = True
while ismeteld:
    szam = input("Kérek egy egész számot: ")
    if szam.isdecimal():
        egesz=int(szam)
        ismeteld = False
print(egesz)


print("Alma12ékes".isalnum())
print("Alma12ekes".isalnum())


lista = ["alma","barack","szilva"]
print(" vettem ".join(lista)) # helyköz
print(",".join(lista))

x = ",".join(lista)
print(x.split(","))
