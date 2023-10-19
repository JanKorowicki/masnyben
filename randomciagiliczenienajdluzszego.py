import random
slowa = ""
slowo = ""
y = 0

while y < 100:
    for x in range(random.randint(1, 10)):
        liczba = random.randint(0, 1)
        if liczba == 0:
            slowo += "A"
        if liczba == 1:
            slowo += "B"
    slowa += slowo
    slowo = ""
    y += 1

print(slowa)
p = slowa[0]
max = 0
cag = 0
znak = 0
mznak = 0
for x in slowa:
    znak += 1
    if x == p:
        cag +=1
        if cag > max:
            max = cag
            mznak = znak

    else:
        cag = 0
    p = x
print(f"najdluzszy ciag ma {max} liter")
print(f"zaczyna sie na {mznak - max} miejscu i sie konczy na {mznak} miejscu")