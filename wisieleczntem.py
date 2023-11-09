import random
import requests
def getslowa():
    try:
        response = requests.get('https://random-word-api.herokuapp.com/word')
        return response.json()[0]
    except:
        slowa = ["wisielec", "auto", "zupa", "yeti", "kupa"]
        return random.choice(slowa)

def gra(slowo):
    kod = "#"*len(slowo)
    proby = 7
    podane_slowa = []
    print("zgadnij slowo:")
    print(kod)
    while proby >= 0:
        zgad = input()
        zgad = zgad.lower()
        if len(zgad) == 1:
            if zgad in slowo:
                print("Dobrze!")
                for y, x in enumerate(slowo):
                    if zgad == x:
                        kod = kod[:y] + zgad + kod[y + 1:]
            else:
                print("Żle")
                if zgad not in podane_slowa:
                    proby -= 1
            print(f"masz jeszcze {proby} prób")
            print(kod)
            if slowo == kod:
                print("WYGRAŁEŚ!!")
                break
            elif proby <= 0:
                print("PRZGRAŁEŚ :(")
                break
            if zgad not in podane_slowa:
                podane_slowa.append(zgad)
        else:
            print("za duzo liter, podaj jedna litere")
            print(f"masz jeszcze {proby} prób")
            print(kod)
gra(getslowa())