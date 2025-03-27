import random
import time

def display_intro():
    print('''You are in a land full of dragons. In front of you , you see two caves. In one cave, the dragon is friendly
          and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight''')
    

    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print("Which cave will you go into? (1 or 2)")
        cave = input

    return cave

def checkcave(chosencave):
    print("You approach the cave.....")
    time.sleep(2)
    print("It is dark and spooky.....")
    time.sleep(2)
    print("A large dragons jumps out at you, he opens his jaws and.....")
    print()
    time.sleep(2)

    friendly_cave = random.randint(1, 2)

    if chosencave == str(friendly_cave):
        print("Gives you his treasure!")
    else:
        print("Gobbles you down in one bite!")

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'Y':
    display_intro()
    caveNumber = chooseCave()
    checkcave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()