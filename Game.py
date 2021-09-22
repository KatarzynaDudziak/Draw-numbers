from random import randint
import time
import Player, Config

class Game:
    def __init__(self, selectedNumbers=None, drawnNumbers=None, hitNumbers=None, config=None):
        self.selectedNumbers = selectedNumbers
        self.drawnNumbers = drawnNumbers
        self.hitNumbers = hitNumbers
        self.config = config

    def choose_level(self, configs, player: Player):
        retryInput = True
        while retryInput:
            print(f"{player.name}, choose difficulty level: ")
            i = 1

            for element in configs:
                print(f"{i} - {element.difficulty}")
                i += 1

            try:
                level = int(input()) - 1
                if level < 0 or level >= len(configs):
                    print(f"{player.name} the selected level is incorrect!")
                else:
                    print(f"{player.name} you selected level: {level + 1}")
                    self.config = configs[level]
                    retryInput = False
            except:
                print("Please, select a level from the given.")

    def get_config(self) -> Config:
        return self.config

    def get_numbers(self):
        print(
            f"Enter your {self.config.playerNumbers} unique numbers from "
            f"{self.config.startOfRange} to {self.config.endOfRange} separated by a comma:")

        self.selectedNumbers = set(int(x) for x in input().split(","))
        elements = []

        for x in self.selectedNumbers: 
            if x in range(self.config.startOfRange, self.config.endOfRange):
                elements.append(x)
            else:
                print("Wrong data. You should use numbers from the given range.")
        return self.selectedNumbers

    def is_numbers_valid(self, setSelectedNumbers):
        if len(setSelectedNumbers) != self.config.playerNumbers:
            return False
        return True

    def start_draw(self):
        print("Let's start the draw!")
        time.sleep(2)

    def draw_numbers(self):
        self.drawnNumbers = set()

        while len(self.drawnNumbers) < self.config.playerNumbers:
            randomNumber = randint(self.config.startOfRange, self.config.endOfRange)
            self.drawnNumbers.add(randomNumber)
        print(f"The drawn numbers: {self.drawnNumbers}")
        return self.drawnNumbers

    def find_hit_numbers(self, setSelectedNumbers, drawnNumbers):
        self.hitNumbers = setSelectedNumbers & drawnNumbers
        if len(self.hitNumbers) == 0:
            print("Unfortunately, it's not your time. Try again! :)")
        else:
            time.sleep(1)
            print(
                f"You hit {len(self.hitNumbers)} numbers! :)"
                f"These numbers are : {self.hitNumbers}!")
        return self.hitNumbers

    def calculate_points(self, winNumbers):
        return len(winNumbers) * self.config.points

    def play_again(self):
        print("Do you want to play again? y/n")
        answer = input()

        if answer.lower() == "y":
            return True
        return False
