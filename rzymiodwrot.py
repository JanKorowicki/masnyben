data = input("podaj date w rzymskich na capsie: ")
znak = 0
datak = 0


for x in range(len(data)):
    if data[x] == "M":

        if znak == 0:
            datak = datak + 1000
        elif znak >= 1000:
            datak = datak + 1000
        elif znak < 1000:
            datak = datak - 2 * znak + 1000

        znak = 1000
    elif data[x] == "D":

        if znak == 0:
            datak = datak + 500
        elif znak >= 500:
            datak = datak + 500
        elif znak < 500:
            datak = datak - 2 * znak + 500


        znak = 500
    elif data[x] == "C":

        if znak == 0:
            datak = datak + 100
        elif znak >= 100:
            datak = datak + 100
        elif znak < 100:
            datak = datak - 2 * znak + 100


        znak = 100
    elif data[x] == "L":
        if znak == 0:
            datak = datak + 50
        elif znak >= 50:
            datak = datak + 50
        elif znak < 50:
            datak = datak - 2 * znak + 50


        znak = 50
    elif data[x] == "X":

        if znak == 0:
            datak = datak + 10
        elif znak >= 10:
            datak = datak + 10
        elif znak < 10:
            datak = datak - 2 * znak + 10


        znak = 10
    elif data[x] == "V":

        if znak == 0:
            datak = datak + 5
        elif znak >= 5:
            datak = datak + 5
        elif znak < 5:
            datak = datak - 2 * znak + 5


        znak = 5
    elif data[x] == "I":

        if znak == 0:
            datak = datak + 1
        elif znak >= 1:
            datak = datak + 1
        elif znak < 1:
            datak = datak - 2 * znak + 1


        znak = 1
    else:
        print("awaria")
        break
if datak <= 3000:
    print(datak)
else:
    print("Awaria")

rzym = int(input("Podaj znaki rzymskie do przetlumaczenia: "))
konc = ""

while (rzym > 0):
    if (rzym - 1000 >= 0):
        rzym -= 1000
        konc += "M"

    elif (rzym - 900 >= 0):
        rzym -= 900
        konc += "CM"

    elif (rzym - 500 >= 0):
        rzym -= 500
        konc += "D"

    elif (rzym == 400):
        rzym -= 400
        konc += "CD"

    elif (rzym - 100 >= 0):
        rzym -= 100
        konc += "C"

    elif (rzym - 90 >= 0):
        rzym -= 90
        konc += "XC"

    elif (rzym - 50 >= 0):
        rzym -= 50
        konc += "L"

    elif (rzym - 40 >= 0):
        rzym -= 40
        rzym += "XC"

    elif (rzym - 10 >= 0):
        rzym -= 10
        konc += "X"

    elif (rzym - 9 >= 0):
        rzym -= 9
        konc += "IX"

    elif (rzym - 5 >= 0):
        rzym -= 5
        konc += "V"

    elif (rzym - 4 >= 0):
        rzym -= 4
        konc += "IV"

    elif (rzym - 1 >= 0):
        rzym -= 1
        konc += "I"



print(konc)