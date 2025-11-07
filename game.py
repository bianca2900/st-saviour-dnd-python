import random
import time

from player import Player
from draw import draw_d20, draw_d6, draw_d4

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    # create character by collecting user input (name + class)
    # print character sheet
    # specify roll that must be beat and enemy initiative by collecting user input
    # any buffs / debuffs?
    # any critical success / failure?

    # player_1 = Player('Bianca', 'Doctor', 10)
    # player_1.attack() THIS WAS ALL MEEE

    # player_2 = Player('Miranda', 'Barbarian', 20)
    # player_2.attack() THIS WAS ALL MEEE

    input('Press enter to roll a 6-sided die. ')
    roll = random.randint(1, 6)
    name = ''
    if roll == 1 or roll == 2:
        name = 'Mr. Mint'
    if roll == 3 or roll == 4:
        name = 'Ms. Candy Cane'

    player = Player(name, )


    role = input('Role: ')

    # player = Player(name, role, 10) THIS WAS MEEE
    # print('Your name is ' + player.name + ' and your role is ' + player.role + '.') #  I ADDED TO THIS
    # print_dramatic_text('Our adventure begins in a shady tavern ...')

    # input('Press Enter to roll a d20.')
    # roll = random.randint(1, 20)
    # draw_d20(roll)
