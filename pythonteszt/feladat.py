def osszead(szam1, szam2):
    """ A függvény két számot kap és 
        visszatér a két szám összegével.
    """
    # YOUR CODE HERE
    return szam1+szam2
    raise NotImplementedError()
# Ellenőrizd a függvényt a cella futtatásával! 
# Az assert csak hiba esetén ad visszajelzést.

assert osszead(14, -8) == 6
'''
Feladat: Melyik a kisebb? (2 pont)
Írj egy függvényt kisebb néven,
amely két számot kap és
visszatér a kisebbel.
'''
def kisebb(szam1, szam2):
    """ A függvény két számot kap és 
        visszatér a kisebbel.
    """
    # YOUR CODE HERE
    if szam1 < szam2:
        return szam1
    else:
        return szam2
    raise NotImplementedError()
# Ellenőrizd a függvényt a cella futtatásával! 
# Az assert csak hiba esetén ad visszajelzést.

assert kisebb(10, -7) == -7
assert kisebb(-10, 7) == -10
'''
Feladat: Melyik a nagyobb? (2 pont)
Írj egy függvényt nagyobb néven,
amely két számot kap és
visszatér a nagyobbal.
'''
def nagyobb(szam1, szam2):
    """ A függvény két számot kap és 
        visszatér a nagyobbal.
    """
    # YOUR CODE HERE
    if szam1 > szam2:
        return szam1
    else:
        return szam2
    raise NotImplementedError()
# Ellenőrizd a függvényt a cella futtatásával! 
# Az assert csak hiba esetén ad visszajelzést.

assert nagyobb(12, -8) == 12
assert nagyobb(-12, -8) == -8 
'''
Feladat: Számtani közép (2 pont)
Írj szamtani_kozep néven függvényt,
amely két számot kap bemenetként és
visszatér a számtani középpel.
'''
def szamtani_kozep(szam1, szam2):
    """ A függvény két számot kap és 
        visszatér a számtani középpel.
    """
    # YOUR CODE HERE
    return (szam1+szam2) / 2
    raise NotImplementedError()
# Ellenőrizd a függvényt a cella futtatásával! 
# Az assert csak hiba esetén ad visszajelzést.

assert szamtani_kozep(3, 5) == 4.0
'''
Feladat: Négyzet kerülete (2 pont)
Írj negyzet_kerulet néven függvényt,
amely egy négyzet oldalhosszát kapja bemenetként és
visszatér a négyzet kerületével.
'''
def negyzet_kerulet(oldal):
    """ A függvény egy négyzet oldalhosszát kapja bemenetként és 
        visszatér a négyzet kerületével.
    """
    # YOUR CODE HERE
    return oldal * 4
    raise NotImplementedError()
# Ellenőrizd a függvényt a cella futtatásával! 
# Az assert csak hiba esetén ad visszajelzést.

assert negyzet_kerulet(5.1) == 20.4
'''
Feladat: Négyzet területe (2 pont)
Írj negyzet_terulet néven függvényt,
amely egy négyzet oldalhosszát kapja bemenetként és
visszatér a négyzet területével.
'''
def negyzet_terulet(oldal):
    """ A függvény egy négyzet oldalhosszát kapja bemenetként és 
        visszatér a négyzet területével.
    """    
    # YOUR CODE HERE
    return oldal * oldal
    raise NotImplementedError()
# Ellenőrizd a függvényt a cella futtatásával! 
# Az assert csak hiba esetén ad visszajelzést.

assert negyzet_terulet(5.0) == 25.0
'''
Feladat: Téglalap kerülete (2 pont)
Írj teglalap_kerulet néven függvényt,
amely egy téglalap oldalhosszait kapja bemenetként és
visszatér a téglalap kerületével.
'''
def teglalap_kerulet(oldal1, oldal2):
    """ A függvény egy téglalap oldalhosszait kapja bemenetként és 
        visszatér a téglalap kerületével.
    """
    # YOUR CODE HERE
    return 2 * (oldal1+oldal2)
    raise NotImplementedError()
# Ellenőrizd a függvényt a cella futtatásával! 
# Az assert csak hiba esetén ad visszajelzést.

assert teglalap_kerulet(5, 6) == 22