# wassup ya little shit. you a nerd if u seeing this so enjoy.
# but before yall start complaining, this breaks the fourth wall a bit
# its python btw


print('Attck has  CHANCE of dropping a rare item.') # guide
print('all mobs need more or = to 6 damage for them to die')
print('food may be contaminated. if it is, you will lose 4 health points. you have 10')
print('you go wandering around in a forest')
print('if u kill the firat grem, u die cuz he releses a toxic gas')
grem1 = input(" and you find a gremlin. what do you do (Attack or leave): ")
if grem1.lower() == 'attack':
    import random

    random_int1 = random.randint(1, 10)

    print(f"you have delt {random_int1} damage!")
if random_int1 < 6:
    print('sadly you have not killed the monster!')
    yippee = input('attack or leave: ')
if random_int1 == 6:
    print('yippee, you killed the gremlin')
    print('you got a Quarter. this will be usefull later! (WIP)')
if yippee.lower() == 'leave':
 dir = input('you have left. while leaving, you find a intersection, which way are you going to go (left, right): ')
if dir.lower() == 'left':
    print('there was another gremlin, it came up by suprise and killed you. restart.')
if dir.lower() == 'right':
    print('while going right, your stoumach is grumbling, you find a vending machine')

choiceq = input(f"are you going to use it? (yes or no): ")
if choiceq.lower() == 'yes':
    eat = True
    print(" you have now eaten")
if choiceq.lower() == "no":
    print('you dead. restart.')

if choiceq.lower() == 'yes':
    print(' you got potato chippys')
    print('you have no mo quarter')
if random_int1 > 6:
    print(f"you hungwy prob")
    print(f"eaten??: {eat}")
if eat == True:
    print('you not hungry')
if eat == False:
    print('i didnt properly code this and this is my first project so cut me some slack')
eatend2 = input('you have not ate. but you find a vending machone. will you use ur only quarter? (yes, no): ')
if eatend2.lower() == 'yes':
    print('well yipee. you spent your only quarter on chips. crazy')
if eatend2.lower() == 'no':
    print("im too tired for this shit. save all u want, its 2 am for me gn")
