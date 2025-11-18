import random

class Player: 
    def __init__(self, name: str):
        self.name = name
        self.location = 0
        self.finish = False

    def roll_dice(self) -> int:
        roll = random.randint(1, 6)
        return roll
    
    def move(self, steps: int) -> None:
        if steps < 0 and self.location <= abs(steps):
            self.location = 0
            return
        self.location += steps
        if self.location >= 10:
            self.finish = True
    