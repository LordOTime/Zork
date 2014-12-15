import time
import sys
import random

class luke1:
  def __init__(self, species, legs, color):
    self.species = species
    self.legs = legs
    self.color = color
        
luke = luke1('Doctor Who fanatic', 2, 'white')
sam = luke1('Wizard', 2, 'Perfectly tanned')
print('Let us learn about two muggles named Luke and Sam! Press enter to continue.')
userName=raw_input();
print "In this educational guide, you must capitalize the first letter of phrase you enter. Have much fun!!!{}.".format(userName)
sys.stdout.flush()
time.sleep(3)
print('Say Ok if you would like to continue')
learn = raw_input('Type here: ')
if learn == 'Ok':
  print('Alright then')
else:
  print('Go away then...')
print('I can tell you what species they are, how many legs they have, or what their natural skin color is!')
info_input = [sam.species, sam.legs, sam.color, luke.species, luke.legs, luke.color]
input_1 = raw_input('Type \'Species\', \'Legs\', or \'Color\':')
if input_1 == 'Species':
  print('Do you want to know about Luke or Sam?')
  input_1 = raw_input('Type Luke or Sam to become an educated being: ')
  if input_1 == 'Sam':
    print(sam.species)
  if input_1 == 'Luke':
    print(luke.species)
elif input_1 == 'Legs':
  print('Do you want to know about Luke or Sam?')
  input_1 = raw_input('Type Luke or Sam to become an educated being: ')
  if input_1 == 'Sam':
    print(sam.legs)
  if input_1 == 'Luke':
    print(luke.legs)
elif input_1 == 'Color':
  print('Do you want to know about Luke or Sam?')
  input_1 = raw_input('Type Luke or Sam to become an educated being: ')
  if input_1 == 'Sam':
    print(sam.color)
  if input_1 == 'Luke':
    print(luke.color)
print("You know what? I like you. Your free! There is only one problem, I do not remember who you learned about.")
print('Sorry my memory is awful sometimes.')
print('Can you type the name of the person who you learned about for me? In fact if you do, I\'ll make a text-based adventure game just for you! Put yourself in their shoes as they go on this epic quest. Whom did you learn about? Choose Luke or Sam.')
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
  print("Wizard's hat")
  print("Knight's helmet")
  print("Fez")
  print("No thanks")
  print(' ')
  hat = raw_input('Your choice of hat:')
  if hat == "Wizard's hat":
    hat = "Wizard"
    print("\"Excellent choice!\"")
  elif hat == "Knight's helmet":
    hat = "helmet"
    print("\"Excellent choice!\"")
  elif hat == "Fez":
    hat = "cool"
    print("\"Excellent choice!\"")
  elif hat == "No thanks":
    hat = "None"
    print("\"Very well.\"")
  print("You return to the courtyard.")
elif shop == "The Jolly Man's Cave":
  print("You enter the cold dark tavern. A smell of sweat and blood are in the air. A large group is in the center of the tavern and are shouting\"Fight! Fight!, Fight!\" immediatly you know this is the wrong choice. As you turn to leave a huge man takes your arm and drags you into the center of all the chanting.")
  print("You are stuck in the ring and have no way to get out, but you have a choice on who you would like to fight.")
  print(" ")
  print("A Scrawny Man")
  print("The Giant Man")
  print("The Tavern's Owner")
  print("Try To Run")
  print(' ')
  fight = raw_input('Your of whom you would like to fight:')
  if fight == "A Scrawny Man":
    fight = "Scrawny Man"
    print("\"Ahhhhh you choose Pete.\"")
    print("The bony man walks into the circle and muters\"you didn't have to do this to yourself %s" % (name))
    print("The man threw a punch with suprising force.")
    print("His giant knuckles made contact with your face.")
    print("Stars are spinning around your head.")
    print(" ")
    print(" ")
  elif fight == "The Giant Man":
    fight = "Giant man"
    print("\"Excellent choice!\"")
    print("You may acctually stand a chance!")
    print("The man lumbered into the circle. The circle seemed too small for the Giant of a man!")
    print("\"Let's hope that you can make friends with me in the next 30 seconds because if you don't you will be in a world of hurt.\" The man said")
  elif fight == "The Tavern's Owner":
    fight = "Tavern Owner"
    print("\"Hey at least when you get knocked out, have your head smash into the ground, and have your teeth get lost in the cobble stone floor you can have some whisky to numb the pain\" A man yelled out in a sarcastic tone.")
  elif fight == "Try To Run":
    fate_1 = 'Escape'
    fate_2 = 'Get trapped'
    fate_3 = [fate_1, fate_2]
    fate_4 = (random.choice(fate_3))
    if fate_4 == fate_1:
      print(fate_1)
    else:
      print(fate_2)



    