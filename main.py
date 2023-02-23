count = 0

for zmienna in range (1, 101):
    if (zmienna % 5 == 0) and (zmienna % 3 == 0):
        print("FizzBuzz")
    elif zmienna % 3 == 0:
        print("Fizz")
        count = count + 1
    elif zmienna % 5 == 0:
        print("Buzz")
    else:
        print(zmienna)

print(f"wypisało fizz {count} razy")
