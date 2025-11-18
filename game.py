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
    print_dramatic_text("The random character generator will give you your character")
    input('Press Enter to draft a random character. ')
    roll = random.randint(0, 4)

    first_names = [
        'Mr. Mint',
        'Princess Frosting',
        'Gloppy'
    ]

    second_names = [
        'Lord Licorice',
        'Princess Lolly',
        'Princess Candycane'
    ]

    name = first_names[random.randint(0, 2)]
    player_1 = Player(name)

    name = second_names[random.randint(0, 2)]
    player_2 = Player(name)
    
    print_dramatic_text('Welcome Player 1 you are ' + player_1.name)
    print_dramatic_text('Welcome Player 2 you are ' + player_2.name)

    while not player_1.finish and not player_2.finish:

        print('------ next player\'s turn -------')

        # player 1's turn
        input(player_1.name + ' press Enter to draw a card! ')
        steps = random.randint(-1, 5)
        draw_card(steps)
        player_1.move(steps)
        print_dramatic_text(player_1.name + ' moves ' + str(steps) + '!')
        print(player_1.name + '\'s location: ' + str(player_1.location))

        print('------ next player\'s turn -------')

        # player 2's turn
        input(player_2.name + ' press Enter to draw a card! ')
        steps = random.randint(-1, 5)
        draw_card(steps)
        player_2.move(steps)
        print_dramatic_text(player_2.name + ' moves ' + str(steps) + '!')
        print(player_2.name + '\'s location: ' + str(player_2.location))

    if player_1.finish:
        print_dramatic_text('Congratulations ' + player_1.name + ' you have reached King Kandy!')
        print_dramatic_text('You have won the game. Here is your prize:  >@< >@< >@< >@< >@<.')
        print_dramatic_text('Now you get to have these candies to share with all of your friends!!!')
        print_dramatic_text('Congratulations!:)')
    else:
        print_dramatic_text('Congratulations ' + player_2.name + ' you have reached King Kandy!')
        print_dramatic_text('You have won the game. Here is your prize:  >@< >@< >@< >@< >@<.')
        print_dramatic_text('Now you get to have these candies to share with all of your friends!!!')
        print_dramatic_text('Congratulations!:)')
    
