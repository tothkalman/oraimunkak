import random

def genLista(db,kezd=1,veg=100):
    listam = list()
    for _ in range(db):
        #print(random.randint(1,100))
        listam.append(random.randint(kezd,veg))
    return listam

l=genLista(10,20,30)
print(l)
'''
l2=genLista(10,1,45)
print(l2)

l3=genLista(10) # 1 és 100 között alapértelmezett
print(l2)
'''
# másolás
def masolas(lista):
    lista2 = list()
    for elem in lista:
        lista2.append(elem*2)
    return lista2
print(masolas([3,7,1,4,6,14,2,8]))

# kiválogatás
def kivalogatas(lista):
    lista2 = list()
    for elem in lista:
        if elem % 2 == 0: # páros szám
            lista2.append(elem)
    return lista2
print(kivalogatas(l))

# maximum 2
def maximum(lista):
    max = lista[0]
    for elem in lista:
        if elem > max:
            max = elem
    return max
print(maximum(l))