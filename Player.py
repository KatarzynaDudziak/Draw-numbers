import time

class Player:
    def __init__(self, name="", playerPoints=0):
        self.name = name
        self.playerPoints = playerPoints
        self.input_name()

    def input_name(self):
        print(f"Enter your name:")
        self.name = input()

        if self.name == "":
            self.name += "player"

    def get_name(self):
        return self.name

    def add_points(self, newPoints):
        self.playerPoints = self.playerPoints + newPoints
        print(
            f"You get {newPoints} points "
            f"Now you have {self.playerPoints} points")
        time.sleep(1)
        return self.playerPoints