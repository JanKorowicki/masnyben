import random


hp = 20#STATYSTYKI
ma = 20
dmg = 2
ehp = 45
edmg = 3
move = 0
crit = 0
critchance = 7
mdmg = 5
maregen = 2
role = 0
enemychose = 0
killstreak = 0
poteq = ["health potion"]
wybpot = 0
potchance = 0
lospot = 0
def win():#winowanie albo przegrywanie
	print("Congrats! You Killed your enemy! Now it's time for the next one.")
	return 0
def lost():
	print("WASTED :(")
	return 0
def clean():#fake clear ekranu
	print("\n" * 30)
	return 0

print("It looks like you have fallen into the dungeons. Now you have to survive")
print("------------------------------------------------------")
print("But first choose tour role: ")#Wybor ról
print("(1)Knight: hp = 40, mana = 10, dmg = 5, mana dmg = 2")
print("(2)Mage: hp = 20, mana = 30, dmg = 1, mana dmg = 5")
print("(3)Assasin: hp = 20, mana = 15, dmg = 8, mana dmg = 3")
print("(4)Crusader: hp = 60, mana = 20, dmg = 3, mana dmg = 3")
print("------------------------------------------------------")
while 1:
	role = input("Which role do you choose?: ")

	if (role == "1"):
		hp = 40
		ma = 10
		dmg = 5
		mdmg = 2
		break
	elif (role == "2"):
		hp = 20
		ma = 30
		dmg = 1
		mdmg = 5
		break
	elif (role == "3"):
		hp = 20
		ma = 15
		dmg = 8
		mdmg = 3
		break
	elif (role == "4"):
		hp = 60
		ma = 20
		dmg = 3
		mdmg = 3
		break
	else:
		print("thats not an option")

clean()
while 1:
	crit = random.randint(1, 10)#MECHANIZM KRYTUJĄCY
	potchance = random.randint(1, 10)#LOSOWANIE POTKI

	print("---------------------")
	print(f"ENEMY-- hp: {ehp}")#INTERFEJS
	print(f"\n hp: {hp} \n mana: {ma} \n dmg: {dmg}")
	print(f"\n Melee Attack(1)({dmg} dmg), Magic Attack(2)({mdmg} mdmg), Heal(3)({mdmg} hp), Ultimate(4)({ma} dmg)", end = ", ")
	if (role == "1"):
		print("Mega Slash(5)(15 dmg)")
	elif (role == "2"):
		print("Abra Kadabra(5)(20 dmg)")
	elif (role == "3"):
		print("Backstab(5)(20 dmg)")
	elif (role == "4"):
		print("Holy strike(5)(15 dmg)")
	print("to open potions menu press 9")
	print("---------------------")

	if (hp <= 0):#KONIEC GRY
		lost()
		print(f"You killed {killstreak} opponents")
		break
	if (ehp <= 0):#dawanie nowego przeciwnika