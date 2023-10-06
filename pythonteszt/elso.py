
print(34+3)
print("Szia"+" "+"!")
print("Szia"+" "+"!"*3) # szöveg szorozható
# print("Szia"+9+"!") TypeError
print("Szia",end=" ")
print("barátom!")
# egymás melletti print ^^
print("Szia",end="-"*5)
print("barátom!")
#
print("1234\n\n567\n89")
print("1234\b567") # \b back space
print("1234\f567") # \f alatta levő sorra rakja a következő szöveget (új lapra rakja, nyomtatásnál van)
print("1234\t567") # \t több spacet rak
print("1234\r567") # \r sor elejére rakja az előtte levő szöveget
print("1234\a567") # \a be van jelölve mint használható cucc, de nem csinál semmit
print("1234\x567") # \x
print("1234\v567") # \v ugyanolyan mint \f
print("1234\"567")
print('1234\'567')
print('1234\\567')
print('1234\567')
# ascii table használata (https://commons.wikimedia.org/wiki/File:ASCII-Table-wide.pdf)
print("\x41\x41") # x41 = AA
print("a\102c") # 102 = B
# ''' vagy """ több soros comment
x=12
y=13
print("x =",x,";","y =",y)
print(1,',',2,',',3,',',4,',',5)
print(1,2,3,4,5,sep=", ") # egymás közti szöveghez ír valamit
print(x,"*",y,"=",x*y)
#
x=+1
print("x =",x,";","y =",y)
x+=1 # x = x + 1
print("x =",x,";","y =",y)
#
x="Alma"
print("x =",x,";","y =",y)
print(x,"*",y,"=",x*y)
print(x,"*",y,"=",y*x)
# mindegy hogy írod ^

ezMi = 1 == 1 # bool class
print(type(ezMi),ezMi)
ezMi = 1 == 2
print(type(ezMi),ezMi)
ezMi = 1 < 2
print(type(ezMi),ezMi)
# == ; < ; > ; <= ; >=