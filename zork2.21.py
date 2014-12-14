#!/usr/bin/python
print("What is your name?")
name = raw_input()
print(' ')
print "Welcome to Zork 2.0, %s. Your adventure starts here." % (name)
print("You find yourself standing in the courtyard in the middle of a grand castle. Beneath your feet are gray cobbles, and you are surrounded my many bustling shops, inns, and pubs. Choose one of the selections to enter.")
print(' ')
print("The Jolly Man's Cave")
print("The Crown Inn")
print("Ye Olde Hat Shoppe")
print("Old Bucktooth's")
print("The Gilded Lilly")
print(' ')
shop = raw_input('your choice of establishment:')
if shop == "Ye Olde Hat Shoppe":
	print("You enter the shop, and, as expected, it is filled with hats of all kinds. There is a tall, thin, pale man behind the counter who asks, \"Would you like to buy a hat?\"")
	print
	print("Wizard hat")
	print("Knight's helmet")
	print("Fez")
	print("No thanks")
	print(' ')
	hat = raw_input('your choice of hat:')
	if hat == "Wizard hat":
		hat = "wizard"
		print("\"Excellent choice!\"")
	elif hat == "Knight's helmet":
		hat = "helmet"
		print("\"Excellent choice!\"")
	elif hat == "Fez":
		hat = "cool"
		print("\"Excellent choice!\"")
	elif hat == "No thanks":
		hat = "none"
		print("\"Very well.\"")
	print("You return to the courtyard.")