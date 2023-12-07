teraz = ""
wczesniej = ""
liczbazmian = 0
punA = 0
punB = 0
wygrane = []
passa = 0
makspassa = 0
passy = 0
wlasmakspassy = ""

with open('mecz.txt') as wyniki:
    wyniki = wyniki.read()
    for x in wyniki:
        teraz = x
        if teraz == wczesniej:
            passa += 1
        if passa >= 10 and teraz != wczesniej:
            passy += 1
        if passa > makspassa:
            makspassa = passa + 1
            wlasmakspassy = x
        if teraz != wczesniej:
            liczbazmian += 1
            passa = 0
        wczesniej = x
        if x == "A":
            punA += 1
        if x == "B":
            punB += 1
        if punA >= 1000 and punA - punB >= 3:
            wygrane.append("A")
            wygrane.append(punA)
            wygrane.append(punB)
            punA = 0
            punB = 0
            passa = 0
        if punB >= 1000 and punB - punA >= 3:
            wygrane.append("B")
            wygrane.append(punB)
            wygrane.append(punA)
            punA = 0
            punB = 0
            passa = 0

print(liczbazmian - 1)
print(f"1 mecz wygrala druzyna {wygrane[0]} wynikiem {wygrane[1]}:{wygrane[2]}")
print(f"bylo {passy} pass, a najwieksza wynosila {makspassa} i zostala zrobiona przez druzyne {wlasmakspassy}")
