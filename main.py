from random import randint
import time


class Player:
    def __init__(self, name="", level=1, playerPoints=0):
        self.name = name
        self.playerPoints = playerPoints
        self.level = level


class Config:
    def __init__(
            self, startOfRange, endOfRange, playerNumbers,
            difficulty, points):
        self.startOfRange = startOfRange
        self.endOfRange = endOfRange
        self.playerNumbers = playerNumbers
        self.difficulty = difficulty
        self.points = points


def get_name():
    print(f"Enter your name:")
    name = input()

    if name == "":
        name += "player"

    return name


def choose_level(player, configs):
    print(f"{player.name}, choose difficulty level: ")
    i = 1

    for element in configs:
        print(f"{i} - {element.difficulty}")
        i += 1

    playerConfig = input()

    try:
        return int(playerConfig)
    except ValueError:
        return -1


def is_level_correct(configs, player):
    if player.level <= 0 or player.level > len(configs):
        return False
    return True


def get_numbers(config: Config):
    print(
        f"Enter your {config.playerNumbers} unique numbers from "
        f"{config.startOfRange} to {config.endOfRange} separated by a comma:")
    selectedNumbers = input()

    try:
        return set(int(x) for x in selectedNumbers.split(","))
    except:
        return -1


def is_numbers_valid(setSelectedNumbers, config: Config):
    if len(setSelectedNumbers) != config.playerNumbers:
        return False
    return True


def draw_numbers(config: Config):
    drawnNumbers = set()

    while len(drawnNumbers) < config.playerNumbers:
        randomNumber = randint(config.startOfRange, config.endOfRange)
        drawnNumbers.add(randomNumber)
    print(f"The drawn numbers: {drawnNumbers}")
    return drawnNumbers


def find_hit_numbers(setSelectedNumbers, drawnNumbers):
    return setSelectedNumbers & drawnNumbers


def calculate_points(winNumbers, config: Config):
    return len(winNumbers) * config.points


def play_again():
    print("Do you want to play again? y/n")
    answer = input()

    if answer == "y":
        return True
    return False


def main():
    player = Player()
    configs = [
        Config(1, 10, 3, "easy", 10),
        Config(1, 50, 5, "medium", 20),
        Config(1, 100, 8, "hard", 40)]
    player.name = get_name()
    replay = True
    while replay:
        player.level = choose_level(player, configs)

        while not is_level_correct(configs, player):
            print(f"{player.name} the selected level is incorrect!")
            player.level = choose_level(player, configs)

        print(f"{player.name} you selected level: {player.level}")
        getNumbers = get_numbers(configs[player.level - 1])

        while not is_numbers_valid(getNumbers, configs[player.level - 1]):
            print(f"You entered the wrong amount of numbers")
            getNumbers = get_numbers(configs[player.level - 1])

        print("Let's start the draw!")
        time.sleep(2)   

        drawnNumbers = draw_numbers(configs[player.level - 1])
        hitNumbers = find_hit_numbers(getNumbers, drawnNumbers)
        if len(hitNumbers) == 0:
            print("Unfortunately, it's not your time. Try again! :)")
        else:
            time.sleep(1)
            print(
                f"You hit {len(hitNumbers)} numbers! :)"
                f"These numbers are : {hitNumbers}!")
        
        newPoints = calculate_points(hitNumbers, configs[player.level - 1])
        player.playerPoints = player.playerPoints + newPoints  
        time.sleep(1)
        if newPoints > 0:
            print(
                f"You get {newPoints} points."
                f"Now you have {player.playerPoints} points")
        else:
            print(f"You have {player.playerPoints} points")
        time.sleep(1)

        replay = play_again()

    print(f"{player.name}, see you next time! :)")

if __name__ == '__main__':
    main()
