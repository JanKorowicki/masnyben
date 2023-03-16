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
if datak < 3000:
    print(datak)
else:
    print("Awaria")