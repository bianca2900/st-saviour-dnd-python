import random
# creates an instance for the players
class Player: 
    def __init__(self, name: str):
        self.name = name # allows the player to have a name
        self.location = 0 # this will say the players will always begin at location 0 
        self.finish = False # this will start off the players with the winning statement always being false

# this will roll a random number from a six sided die
    def roll_dice(self) -> int:
        roll = random.randint(1, 6)
        return roll
    
    def move(self, steps: int) -> None:
        if steps < 0 and self.location <= abs(steps): # says if the number of steps is less than 0 and the location is less than or equal to the absolute value of the steps than the location will be 0 
            self.location = 0
            return
        # this says if the number of steps is greater than or equal to 10 than the finish is true and the code should print the end code
        self.location += steps
        if self.location >= 10:
            self.finish = True
    