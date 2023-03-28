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
		enemychose = random.randint(1,4)#DOBIERANIE PRZECIWNIKA
		lospot = random.randint(1, 3)#DOBIERANIE POTKI
		if (enemychose == 1):#przecziwnik 1
			ehp = 45
			edmg = 5
		if (enemychose == 2):#przeciwnik 2
			ehp = 25
			edmg = 8
		if (enemychose == 3):#przeciwnik 3
			ehp = 100
			edmg = 2
		if (enemychose == 4):#przeciwnik 4
			ehp = 1
			edmg = 2
		if (potchance >= 6):#dodawanie poty do eq po zabiciu przeciwnika z 50% szans na to ze dropnie
			if (lospot == 1):
				poteq.append("health potion")
			elif (lospot == 2):
				poteq.append("mana potion")
			elif (lospot == 3):
				poteq.append("harm potion")

		killstreak += 1
		clean()
		win()
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

	move = input("\n Which attack?: ")#WYBIERANIE ATAKU
	clean()


	if (move == "1"):#ATAK WRECZ
		if (enemychose != 4):
			print("You hit your opponent with an sword")
			if (crit > critchance):#MECHANIZM KRYTUJĄCY I ZADAWANIE DMG
				ehp -= dmg
			else:
				ehp -= dmg*2
			print("And it was CRITICAL")
		else:
			print("Opponents stone skin blocked your attack")
		if (ehp > 0):#DOSTAWANIE DMG
			print(f"But enemy slashed you for {edmg} dmg")
			hp -= edmg
		ma += maregen#REGENERACJA MANY

	elif (move == "2") and (ma >= 4):#MAGICZNY ATAK
		print("You cast a spell on your enemy")
		if (crit > critchance):
			ehp -= mdmg
		else:
			ehp -= mdmg*2
		print("And it was CRITICAL")
		ma -= 4
		if (ehp > 0):
			print(f"But enemy slashed you for {edmg} dmg")
			hp -= edmg
		ma += maregen

	elif (move == "3") and (ma >= mdmg):#healowanie
		print(f"You healed yourself for {mdmg} health and barrierd the enemy attack")
		hp += mdmg
		ma -= mdmg

	elif (move == "4"):  #ULTOWANIE
		print("You ULTED your enemy")
		ehp -= ma
		ma = 0
		if (ehp > 0):
			print(f"But enemy slashed you for {edmg} dmg")
			hp -= edmg
		ma += maregen
	elif (move == "5"):#ATAK SPECJALNY
		if (role == "1") and (ma >= 10):
			if (enemychose != 4):
				print('You used sword mega slash(15 dmg)')
				ehp -= 15
				ma -= 10
			else:
				print("Opponents stone skin blocked your attack")
		elif (role == "2") and (ma >= 20):
			print("You Abra kadabred your enemy(20 mdmg)")
			ehp -= 20
			ma -= 20
		elif (role == "3") and (ma >= 3) and (hp > 1):
			if (enemychose != 4):
				print("You Backstabbed your enemy(20 dmg)")
				ehp -= 20
				ma -= 3
				hp -= 1
			else:
				print("Opponents stone skin blocked your attack")
		elif (role == "4") and (hp > 4):
			print("You Holy Striked your enemy(15 dmg), But it costed you 4 hp")
			ehp -= 15
			hp -= 4
		if (ehp > 0):
			print(f"But enemy slashed you for {edmg} dmg")
			hp -= edmg

	if (move == "9"):#MENU POTEK
		clean()
		print("To leave press 9")
		print("Your potions (type in name to use): ")

		print(poteq)
		wybpot = input("which potion?: ")
		if (wybpot == "health potion") and ("health potion" in poteq):
			hp += 10
			poteq.remove("health potion")
		elif (wybpot == "mana potion") and ("mana potion" in poteq):
			ma += 10
			poteq.remove("mana potion")
		elif (wybpot == "harm potion") and ("harm potion" in poteq):
			ehp -= 5
			poteq.remove("harm potion")
		elif (wybpot == "9"):
			clean()


