import math

def fibo(liczba):
    return round(1/math.sqrt(5)*(((1 + math.sqrt(5))/2)**liczba - ((1 - math.sqrt(5))/2)**liczba))

l = int(input("podaj pozycje: "))
print(fibo(l))

def fibonaczi(liczb):
    if liczb <= 0:
        return 0
    if liczb == 1:
        return 1
    else:
        return fibonaczi(liczb - 1) + fibonaczi(liczb - 2)

print(fibonaczi(l))
