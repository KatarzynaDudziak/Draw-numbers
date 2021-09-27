from random import randint
import time
import Player, Config

class Game:
    def __init__(self, drawnNumbers=None, hitNumbers=None, config=None):
        self.drawnNumbers = drawnNumbers
        self.hitNumbers = hitNumbers
        self.config = config

    def print_configs(self, configs, player: Player):
        print(f"{player.name}, choose difficulty level: ")
        i = 1

        for element in configs:
            print(f"{i} - {element.difficulty}")
            i += 1

    def get_config_from_user(self):
        try:
            level = int(input()) -1
        except:
            level = - 1
        return level

    def choose_config(self, configs, player: Player):
        self.print_configs(configs, player)
        level = self.get_config_from_user()

        while not (level >= 0 and level < len(configs)):
            print(f"{player.get_name()} the selected level is incorrect!")
            self.print_configs(configs, player)
            level = self.get_config_from_user()

        print(f"{player.get_name()} you selected level: {level + 1}")
        self.config = configs[level]

    def get_config(self) -> Config:
        return self.config

    def get_numbers(self):
        print(
            f"Enter your {self.config.playerNumbers} unique numbers from "
            f"{self.config.startOfRange} to {self.config.endOfRange} separated by a comma:")

        try:
            selectedNumbers = set(int(x) for x in input().split(","))
        except:
            return set()
        
        return selectedNumbers

    def is_numbers_valid(self, setSelectedNumbers):
        for x in setSelectedNumbers:
            if not x in range(self.config.startOfRange, self.config.endOfRange):
                print("Wrong data. You should use numbers from the given range.")
                return False

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
