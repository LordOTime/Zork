import time
import sys

class luke1:
  def __init__(self, species, legs, color):
    self.species = species
    self.legs = legs
    self.color = color
        
luke = luke1('Doctor who fanatic', 2, 'white')
sam = luke1('Wizzard', 2, 'Perfectly tanned')
print('Lets learn about two muggles named Luke and Sam! Press enter to continue.')
userName=raw_input();
print "In this educational guide, you must put everything you type in\'\' and capitalize the first letter of everything.Have much fun!!!{}.".format(userName)
sys.stdout.flush()
time.sleep(6)
print('Say \'Ok\' if you would like to continue')
learn = input('Type here: ')
if learn == 'Ok':
  print('Alright then')
else:
  print('Go away then...')
print('I can tell you what species they are, how many legs the have, or what their nateraul skin color is!')
info_input = [sam.species, sam.legs, sam.color, luke.species, luke.legs, luke.color]
input_1 = input('Type \'Species\', \'Legs\', or \'Color\':')
if input_1 == 'Species':
  print('do you want to know about Luke or Sam?')
  input_1 = input('Type \'Luke\' or \'Sam\' to become an educated being: ')
  if input_1 == 'Sam':
    print(sam.species)
  if input_1 == 'Luke':
    print(luke.species)
elif input_1 == 'Legs':
  print('do you want to know about luke or Sam?')
  input_1 = input('Type \'Luke\' or \'Sam\' to become an educated being: ')
  if input_1 == 'Sam':
    print(sam.legs)
  if input_1 == 'Luke':
    print(luke.legs)
elif input_1 == 'Color':
  print('do you want to know about luke or Sam?')
  input_1 = input('Type \'Luke\' or \'Sam\' to become an educated being: ')
  if input_1 == 'Sam':
    print(sam.color)
  if input_1 == 'Luke':
    print(luke.color)
print("You know what? I like you. You no longer have to type \'\' or capitalize the first letter anymore. Your free! There is only one problem, I dont remember who you learned about.")
print('Sorry my memory is aweful sometimes.')
print('Can you type the name of the person who you learned about for me. Infact if you do i\'ll make a text based adventure game just for you! Enter who you learned about here: ')
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
elif shop == "The Jolly Man's Cave":
  print("You enter the cold dark tavern. A smell of sweat and blood are in the air. A large group is in the center of the tavern and are shouting\"Fight! Fight!, Fight!\" immediatly you know this is the wrong choice. As you turn to leave a huge man takes your arm and drags you into the center of all the chanting.")
  print("You are stuck in the ring and have no way to get out, but you have a choice on who you would like to fight.")
  print(" ")
  print("A Scrawny man")
  print("The Giant man")
  print("The tavern's owner")
  print("Try to run")
  print(' ')
  fight = raw_input('Your of whom you would like to fight:')
  if fight == "A scrawny man":
    fight = "Scrawny man"
    print("\"Ahhhhh you choose pete.\"")
    print("The bony man walks into the circle and muters\"you didn't have to do this to yourself %s" % (name))
    print("The man threw a punch with suprising force.")
    print("His giant knukles made contact with your face.")
    print("Stars are spinning around your head.")
    print(" ")
    print(" ")
  elif hat == "Knight's helmet":
    hat = "helmet"
    print("\"Excellent choice!\"")
  elif hat == "Fez":
    hat = "cool"
    print("\"Excellent choice!\"")
  elif hat == "No thanks":
    hat = "none"
    print("\"Very well.\"")