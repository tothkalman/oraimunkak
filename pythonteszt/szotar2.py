mondat = "Minim occaecat consequat dolor irure voluptate esse. Excepteur est Lorem eu dolor laborum ipsum velit ullamco voluptate aute laborum in aute magna."
#print(mondat.lower())
#mondat = mondat.lower()
#print(mondat.replace(".",""))
#mondat = mondat.replace(".","")
#mondat = mondat.replace(" ","")

mondat = mondat.lower().replace(".","").replace(" ","")

print(mondat)

betuk = dict()
'''
for kar in mondat:
    #print(kar)
    if betuk.get(kar) == None:
        betuk.update({kar:1})
    else:
        betuk.update({kar:1+betuk.get(kar)})
print(betuk)
'''
for kar in mondat:
    db = betuk.get(kar)
    if db == None:
        betuk.update({kar:1})
    else:
        #betuk.update({kar:1 + db})
        betuk[kar] += 1
print(betuk)

max = 0 
maxBetu = ""
for k,e in betuk.items():
    if e > max:
        max = e
        maxBetu = k

print(max,maxBetu)

#print("1234".find("a"))

be = input("Kérek egy betűt: ")
if betuk.get(be) == None:
    print(be+" betű nincs a mondatban")
else:
#    print("A "+be+" betű "+ str(betuk.get(be))+" alkalommal szerepelt")
    print(f"A {be} betű {betuk.get(be)} alkalommal szerepelt")

valid = "qwertzuiopasdfghjklyxcvbnm"
while True:
    be = input("Kérek egy angol ABC betűt: ")
    if valid.find(be) >=0 :
        break
print(be)

ismeteld = True
while ismeteld:
    be = input("Kérek egy angol ABC betűt: ")
    if valid.find(be) >=0 :
        ismeteld =False
print(be)

be ="."
while valid.find(be) < 0:
    be = input("Kérek egy angol ABC betűt (rövid): ")

print(be)

be ="."
while not be in valid:
    be = input("Kérek egy angol ABC betűt (rövid): ")

print(be)