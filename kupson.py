
# course = "  Benol Fenol" #<-- string
# print(course)
# print(course.upper())#drukuje course ale na capsie
# print(course.lower())#wszystko z malej drukuje
# print(course.title())#robi z tego tytul
# print(course.lstrip())#l wycina lewa strone a r prawa
# print(course.find("Fe"))#wyszukuje pozycje podanego znaku
# print(course.replace("e", "x"))#zamienia x na y
# print("Be" in course)#sprawdza czy coś znajduje sie w stringu
# print("Be" not in course)#sprawdza czy cos nie znajduje sie w stringu


# print(10 / 3)#dzieli 10 na 3
# print(10 // 3)#to samo + obcina ulamek
# print(10 % 3)#daje nam reszte dzielenia
# print(10 ** 3)#x do potegi y


# import math
# print(round(2.9))#zaokrogla
# print(abs(-2.9))#wartość bezwzględna
# print(math.ceil(2.2))#zaokrągla do góry
# print(math.floor(2.2))#zaokrogla w dol


# x = input("podaj cos: ")
# y = int(x) + 1
# print(f"x: {x}, y: {y}")

# print(ord("a"))#daje nam numer w ascii
# print(ord("b"))

# zmienna = input("podaj zmienna: ")
# if int(zmienna) == 120:
#     print("masnyben")
# else:
#     print("suiiii")


# while 1:
#     wiek = input("podaj wiek: ")
#     if wiek == "koniec":
#         break
#     elif int(wiek) >= 18:
#         print("wkraczamy do akcji")
#     else:
#         print("odwrot")

#for zmienna in range(2,10,2):
    #print(zmienna)


# succesful = True
# for number in range(3):
#     if succesful:
#         print("succesful")
#         break
#     else:
#         print("nie udało sie")

# for x in range(5): #włącz zeby zrozumiec nie da sie opisac(tworzy jakas matryce czy cos)
#     for y in range(3):
#         print(f"{x}, {y}")

# for x in "Python":#string dzila jak tablica
#     print(x)

# for x in [1, 2 ,3 ,4]:
#     print(x)

# count = 0
# for x in range(1, 10):
#     if x % 2 == 0:
#         print(x)
#         count = count + 1
# print(f"bylo {count} liczb parzystych")


# def sranko():
#     print("zesralem sie")
# sranko()


# def dodawanie(x, y=0): #daje funkcje dodawania i y jest domyslnie zero i nie jest wymagane do wpisania
#     print(x + y)
# dodawanie(2, 3)

