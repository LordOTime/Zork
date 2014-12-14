#!/usr/bin/python
print("What is your name?")
name = input('your name:')
print
print "Welcome to Zork 2.0, %s. Your adventure starts here." % (name)
print("You find yourself standing in the courtyard in the middle of a grand castle. Beneath your feet are gray cobbles, and you are surrounded my many bustling shops, inns, and pubs. Choose one of the selections to enter.")
print
print("The Jolly Man's Cave")
print("The Crown Inn")
print("Ye Olde Hat Shoppe")
print("Old Bucktooth's")
print("The Gilded Lilly")
input('your choice of establishment')
print
shop = input()
if shop == "Ye Olde Hat Shoppe":
	print("hat")