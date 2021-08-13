class Player:
    def __init__(self, name="", level=1, playerPoints=0):
        self.name = name
        self.playerPoints = playerPoints
        self.level = level


class Config:
    def __init__(self, startOfRange, endOfRange, playerNumbers, difficulty, points):
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
    print(f"Enter your {config.playerNumbers} unique numbers from "
            f"{config.startOfRange} to {config.endOfRange} separated by a comma:")
    selectedNumbers = input()

    try:
        return set(int(x) for x in selectedNumbers.split(","))
    except:
        return -1


def validated_numbers(setSelectedNumbers, config: Config):
    if len(setSelectedNumbers) != config.playerNumbers:
        return False
    return True


def main():
    player = Player()
    configs = [
        Config(1, 10, 3, "easy", 10),
        Config(1, 50, 5, "medium", 20),
        Config(1, 100, 8, "hard", 40)]
    player.name = get_name()
    player.level = choose_level(player, configs)

    if is_level_correct(configs, player):
        print(f"{player.name} you selected level: {player.level}")
        getNumbers = get_numbers(configs[player.level - 1])
        if getNumbers == -1:
            print("Error: You should choose the numbers from given range")
            exit()
    else:
        print(f"{player.name} the selected level is incorrect!")
        exit()

    if validated_numbers(getNumbers, configs[player.level - 1]) is False:
        print(f"You entered the wrong amount of numbers")
    else:
        print("Let's start the draw!")

if __name__ == '__main__':
    main()
