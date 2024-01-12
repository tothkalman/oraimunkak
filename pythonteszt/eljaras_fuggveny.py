def hasonlit(szam1,szam2):
    if szam1>szam2:
        print(szam1,"nagyobb szám")
    elif szam1<szam2:
        print(szam2,"nagyobb szám")
    else:
        print("A két szám egyenlő")
hasonlit(1,5)
hasonlit(10,5)
hasonlit(5,5)


def osszegzo(lista):
    osz=0
    for elem in lista:
        osz+=elem
    return osz
print(osszegzo([1,2,3,4,5]))

l=[32,54,16]
print(osszegzo(l))

#l=[32,54,16,'a']
l=[32,54,16,78.8]
print(osszegzo(l))