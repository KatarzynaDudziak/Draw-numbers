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


def enter_your_name():
    print(f"Enter your name:")
    name = input()

    return name


def choose_level(player, configs):
    print(f"{player.name}, choose difficulty level: ")
    i = 1

    for element in configs:
        print(f"{i} - {element.difficulty}")
        i += 1

    playerConfig = input()
    return int(playerConfig)


def is_level_correct(configs, player):
    if player.level < 0 or player.level > len(configs):
        return False
    return True


def main():
    player = Player()
    configs = [
        Config(1, 10, 3, "easy", 10),
        Config(1, 50, 5, "medium", 20),
        Config(1, 100, 8, "hard", 40)
    ]
    player.name = enter_your_name()
    player.level = choose_level(player, configs)

    if is_level_correct(configs, player):
        print(f"{player.name} You selected level: {player.level}")
    else:
        print(f"{player.name} the selected level is incorrect!")


if __name__ == '__main__':
    main()