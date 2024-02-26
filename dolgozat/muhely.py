'''
Az adatok beolvasása fájlból,
egy-egy sor az 'adatok' nevű lista egy-egy eleme
'''
adatok = []
with open('autok_listaja.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        # strip() metódus eltávolítja a sorvégi \n-t
        adatok.append(sor.strip())


'''
A 'autok' nevű lista 'auto' nevű szótár típusokat fog tartalmazni,
egy autó adatait egy szótár tárolja
'''
auto = {}  # egy auto adatai
autok = []  # szótárakat tartalmazó lista
for elem in adatok:
    auto_adatai = elem.split()
    auto['rendszam'] = auto_adatai[0]
    auto['marka'] = auto_adatai[1]
    auto['tipus'] = auto_adatai[2]
    auto['kor'] = int(auto_adatai[3])
    if auto_adatai[4] == '1':
        auto['javitva'] = True
    else:
        auto['javitva'] = False
    auto['koltseg'] = int(auto_adatai[5])

    autok.append(auto)
    auto = {}  # egy új, üres szótár objektum deklarálása ugyanazon a néven

#print(autok)

# 3.a feladat
oreg = 0
index = 0
for auto in autok:
    #print(auto)
    if auto['kor'] > oreg:
        oreg = auto['kor']
    index += 1
#print(oreg)
#print(autok[index-1])

print("------------- 3.a feladat -------------")
print(f"A legöregebb autó: {autok[index-1]['rendszam']}, {autok[index-1]['marka']} {autok[index-1]['tipus']}, {autok[index-1]['kor']} éves.")
# ^^^ NE UGYANAZZAL AZ IDÉZŐJELLEL ÍRJ, MERT ÚGY NEM MŰKÖDIK!

# vagy (könnyebb a másik megoldás)

oreg = autok[0]
for auto in autok:
    if auto['kor'] > oreg['kor']:
        oreg = auto

print("------------- 3.a feladat -------------")
print(f"A legöregebb autó: {oreg['rendszam']}, {oreg['marka']} {oreg['tipus']}, {oreg['kor']} éves.")

# 3.b feladat
ossz = 0
for auto in autok:
    ossz += auto['koltseg']

print("------------- 3.b feladat -------------")
print(f"Az egy autóra jutó átlagos javítási költség: {ossz/len(autok)} Ft.")