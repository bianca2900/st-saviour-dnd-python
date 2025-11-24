import random 
import time
# tells the code which files to import
from player import Player
from draw import draw_d20, draw_d6, draw_d4 

# this will deliver the code letter by letter
def print_dramatic_text(text: str, delay=0.05): # this will print the text slowly
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay) # allows the the text to print with very quick pauses
    print()

# this piece of code places the value of the roll into a card like output
def draw_card(value: int) -> None:
    if value >= 0: # this will only draw a number greater than or equal to 0
        print('-------------')
        print('+           +')
        print('+           +')
        print('+     {}     +'.format(value)) # this will input the random number greater than zero that is drawn
        print('+           +')
        print('+           +')
        print('-------------')
    else: # this will draw a number less than 0 
        print('-------------')
        print('+           +')
        print('+           +')
        print('+     {}    +'.format(value)) # this will input a random number that is less than zero
        print('+           +')
        print('+           +')
        print('-------------')

# this piece of code will start the game 
if __name__ == '__main__':
    print_dramatic_text("Welcome to Candy Land! Today you will have to compete with your opponet to get to King Kandy first.")
    print_dramatic_text("First you will have to roll to pick your character.")
    print_dramatic_text("The random character generator will give you your character")
    input('Press Enter to get a random character. ')
    roll = random.randint(0, 4) # this will allow the player to roll a random number to get their random character 

# this will allow the first player to randomly pick from these names listed
    first_names = [
        'Mr. Mint',
        'Princess Frosting',
        'Gloppy'
    ]
# this will allow the second player to randomly pick from the names listed
    second_names = [
        'Lord Licorice',
        'Princess Lolly',
        'Princess Candycane'
    ]

    name = first_names[random.randint(0, 2)] # this will generate a random name from the first name list from the index 0 and the index 2
    player_1 = Player(name) # player one will always have this name

    name = second_names[random.randint(0, 2)] # this will generate a random name from the second name list from the index 0 to the index 2 
    player_2 = Player(name) # player 2 will not be assigned to this name
    
    print_dramatic_text('Welcome Player 1 you are ' + player_1.name) # this will print what is in quotes and add on what player ones name is equal too 
    print_dramatic_text('Welcome Player 2 you are ' + player_2.name) # this will do the same as player one but it will print player twos name 

    while not player_1.finish and not player_2.finish: # this will keep the program going until one of the players has reeached a location greater than or equal to 10

        print('------ next player\'s turn -------') # this will print a divider between each players turn

        # player 1's turn
        input(player_1.name + ' press Enter to draw a card! ') # this will print player ones name plus what is in the single quotes
        steps = random.randint(-1, 5) # this will print the random number of steps between -1 and 5 
        draw_card(steps) # this will print the card we made up with a random number in the middle
        player_1.move(steps) # this allows the player to move the random number of steps
        print_dramatic_text(player_1.name + ' moves ' + str(steps) + '!') # this will print player ones random name plus the word moves and then the random number generated
        print(player_1.name + '\'s location: ' + str(player_1.location)) # this will print the players new location

        print('------ next player\'s turn -------') # this will print a divider between each players turn

        # player 2's turn
        input(player_2.name + ' press Enter to draw a card! ') # this will print player twos name plus what is in the single quotes
        steps = random.randint(-1, 5) # this will print the random number of steps between -1 and 5 
        draw_card(steps) # this will print the card we made up with a random number in the middle 
        player_2.move(steps) # this allows the player to move the random number of steps
        print_dramatic_text(player_2.name + ' moves ' + str(steps) + '!') # this will print player twos random name plus the word moves and then the random number generated
        print(player_2.name + '\'s location: ' + str(player_2.location)) # this will print the players new location

# this will print slowly if player ones location is greater than or equal to 10
    if player_1.finish:
        print_dramatic_text('Congratulations ' + player_1.name + ' you have reached King Kandy!')
        print_dramatic_text('You have won the game. Here is your prize:  >@< >@< >@< >@< >@<.')
        print_dramatic_text('Now you get to have these candies to share with all of your friends!!!')
        print_dramatic_text('Congratulations!:)')
 # this will print slowly if player twos location is greater than or equal to 10   
    else:
        print_dramatic_text('Congratulations ' + player_2.name + ' you have reached King Kandy!')
        print_dramatic_text('You have won the game. Here is your prize:  >@< >@< >@< >@< >@<.')
        print_dramatic_text('Now you get to have these candies to share with all of your friends!!!')
        print_dramatic_text('Congratulations!:)')
    