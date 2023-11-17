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