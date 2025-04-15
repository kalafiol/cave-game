import random
import time 

hp = 100
dragon_hp = 100
print('Welcome to the game cave')
time.sleep(2)
print('You are standing at the entrance of a cave.\nYou have to chose on of the 2 paths so choose wisely')
time.sleep(4)
print('Choose 1 or 2 door')
door_1 = int(input())
if door_1 == 1:
    print('You have chosen door 1')
    time.sleep(2)
    print('You are in a room with a dragon')
    time.sleep(2)
    print('You have to fight the dragon')
    time.sleep(2)
    print('You want to fight the dragon or run away')
    time.sleep(2)
    print('Choose 1 to fight or 2 to run away')
    option_1 = int(input())
    if option_1 == 1:
        print('You have chosen to fight the dragon')
        print('You have 100 health points')
        print('The dragon has 100 health points')
        while hp and dragon_hp > 0:
            random_number_1 = random.randint(10, 20)
            random_number_2 = random.randint(10, 15)
            print(f'You dealt {random_number_1} damage to dragon')
            time.sleep(3)
            print(f'Dragon dealt {random_number_2} damage to you\n')
            hp -= random_number_2
            dragon_hp -= random_number_1
            print(f'You have {hp} health points')
            time.sleep(3)
            print(f'The dragon has {dragon_hp} health points')
            if hp <= 0:
                print('You have died')
            elif dragon_hp <= 0:
                print('You have beaten the dragon\nCoungratulations!!!')
    elif option_1 == 2:
        print('You have chosen to run away')
        time.sleep(2)
        print('You have run away from the dragon')
        time.sleep(2)
        print('You escaped the cave but your not a hero :>')
    else:
        print('Invalid option')
elif door_1 == 2:
    print('You have chosen door 2')
    time.sleep(2)
    print('You are in a room with a treasure')
    time.sleep(2)
    print('You want to open it ?')
    time.sleep(2)
    print('yes or no')
    option_2 = input()
    if option_2 == 'yes':
        print('You have opened the treasure')
        time.sleep(2)
        print('You have found a lot of gold and jewels')
        time.sleep(2)
        print('Congratulations you are now rich')
    elif option_2 == 'no':
        print('You have chosen not to open the treasure')
        time.sleep(2)
        print('You have left the treasure and you are still poor :<')
    else:
        print('Invalid option')
else:
    print('You have to choose one of the 2 doors')





