uczniowie = []
oceny = []

def dodaj_ocene(uczen, ocena):
    uczniowie.append(uczen)
    oceny.append(ocena)
    return True



def usun_ocene(uczen, ocena):
    uczniowie.remove(uczen)
    oceny.remove(ocena)
    return True
wybor = input("chcesz doadać (d), czy usunąć (u): ")
ucze = input("podaj imie ucznia: ")
oce = input("i jego ocene: ")
if wybor == "d":
    dodaj_ocene(ucze, oce)
    print(uczniowie, oceny)
if wybor == "u":
    usun_ocene(ucze, oce)
    print(uczniowie, oceny)
else:
    print("blad")
