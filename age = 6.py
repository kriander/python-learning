import random
import time

def displayIntro():
    ('''You are in a land full of dragons.In front of you,
you will see two caves.In one cave, the dragon is friendly
and will share his treasure with you. the other dragon
 is greedy and hungry, and eat you on sight''')
    print()

def chooseCave():
    cave =''
    while cave != '1' and cave != '2':
        print('witch will you go into (1 or 2)')
        cave = input()

    return cave

def chooseCave(chosenCave):
    print('approach the cave...')
    time.sleep(2)
    print('it is dark and spooky...')
    time.sleep(2)