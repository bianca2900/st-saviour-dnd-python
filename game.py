import random
import time

from player import Player
from draw import draw_d20, draw_d6, draw_d4

def print_dramatic_text(text: str, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def draw_card(value: int) -> None:
    if value >= 0:
        print('-------------')
        print('+           +')
        print('+           +')
        print('+     {}     +'.format(value))
        print('+           +')
        print('+           +')
        print('-------------')
    else:
        print('-------------')
        print('+           +')
        print('+           +')
        print('+     {}    +'.format(value))
        print('+           +')
        print('+           +')
        print('-------------')

if __name__ == '__main__':
    print_dramatic_text("Welcome to Candy Land! Today you will have to compete with your opponet to get to King Kandy first.")
    print_dramatic_text("First you will have to roll to pick your character.")
    print_dramatic_text("The random character generator will give you the character")
    input('Press Enter to draft a random character. ')
    roll = random.randint(0, 4)

    names = [
        'Mr. Mint',
        'Princess Frosting',
        'Gloppy',
        'Lord Licorice',
        'Princess Lolly'
    ]

    name = names[random.randint(0, 4)]
    player_1 = Player(name)

    name = names[random.randint(0, 4)]
    player_2 = Player(name)
    
    print_dramatic_text('Welcome Player 1 you are ' + player_1.name)

    while not player_1.finish:

        input('Press Enter to draw a card! ')
        steps = random.randint(-1, 5)
        draw_card(steps)
        player_1.move(steps)
        print_dramatic_text('You move ' + str(steps) + '!')
        print('Your location: ' + str(player_1.location))

    print_dramatic_text('Congratulations you have reached King Kandy!')
    
