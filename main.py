from Config import Config
from Player import Player
from Game import Game

def main():
    player = Player()
    game = Game()
    configs = [
        Config(1, 10, 3, "easy", 5),
        Config(1, 50, 5, "medium", 10),
        Config(1, 100, 8, "hard", 15)]
    playerName = player.get_name()
    replay = True
    while replay:
        game.choose_config(configs, player)
        playerNumbers = game.get_numbers()

        while not game.is_numbers_valid(playerNumbers):
            playerNumbers = game.get_numbers()
        
        game.start_draw()
        drawnNumbers = game.draw_numbers()
        hitNumbers = game.find_hit_numbers(playerNumbers, drawnNumbers)
        
        winPoints = game.calculate_points(hitNumbers)
        addPoints = player.add_points(winPoints)
        replay = game.play_again()

    print(f"{playerName}, your score is {addPoints}")
    print("See you next time! :)")

if __name__ == '__main__':
    main()
