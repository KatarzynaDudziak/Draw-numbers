from main import *
import pytest
from Player import Player



configs = [
        Config(1, 10, 3, "easy", 5),
        Config(1, 50, 5, "medium", 10),
        Config(1, 100, 8, "hard", 15)]

class TestPlayer():

    def test_create_player_object(self, mocker):
        input_mock = mocker.patch("Player.input")
        input_mock.return_value = "asd"
        Player()
        
    def test_input_valid_name(self, mocker):
        input_mock = mocker.patch("Player.input")
        input_mock.return_value = "tomek"
        player = Player()
        assert player.get_name() == "tomek"

    def test_input_invalid_name(self, mocker):
        input_mock = mocker.patch("Player.input")
        input_mock.return_value = ""
        player = Player()
        assert player.get_name() == "player"

    def test_add_points(self, mocker):
        input_mock = mocker.patch("Player.input")
        input_mock.return_value = ""
        mocker.patch("Player.time")
        player = Player()
        result = player.add_points(5)
        assert result == 5
        result = player.add_points(0)
        assert result == 5
        result = player.add_points(3)
        assert result == 8

class TestGame():

    def test_create_game_object(self):
        Game()

    def test_get_valid_config_from_user(self, mocker):
        input_mock = mocker.patch("Game.input")
        game = Game()
        input_mock.return_value = "1"
        result = game.get_config_from_user()
        assert result == 0
        
    def test_get_invalid_config_from_user(self, mocker):
        input_mock = mocker.patch("Game.input")
        game = Game()
        input_mock.return_value = "w"
        result = game.get_config_from_user()
        assert result == -1
        input_mock.return_value = ""
        result = game.get_config_from_user()
        assert result == -1
        
    def test_choose_valid_config(self, mocker):
        game = Game()
        input_mock = mocker.patch("Game.input")
        input_mock.return_value = "1"
        player_mock = mocker.patch("Game.Player")
        player_mock.get_name.return_value = "player"
        game.choose_config(configs, player_mock)
        assert player_mock.get_name.call_count == 1
        
    def test_choose_invalid_config(self, mocker):
        game = Game()
        input_mock = mocker.patch("Game.input")
        input_mock.side_effect = [4,2]
        player_mock = mocker.patch("Game.Player")
        player_mock.get_name.return_value = "player"
        game.choose_config(configs, player_mock)
        assert player_mock.get_name.call_count == 2
    
    def test_get_valid_numbers(self, mocker):
        game = Game()
        input_mock = mocker.patch("Game.input")
        input_mock.side_effect = ["1", "1,2,3"]
        player_mock = mocker.patch("Game.Player")
        player_mock.get_name.return_value = "player"
        game.choose_config(configs, player_mock)
        result = game.get_numbers()
        assert result == {1,2,3}
    
    def test_get_invalid_character(self, mocker):
        game = Game()
        input_mock = mocker.patch("Game.input")
        input_mock.side_effect = ["1", "a,cd,,"]
        player_mock = mocker.patch("Game.Player")
        player_mock.get_name.return_value = "player"
        game.choose_config(configs, player_mock)
        result = game.get_numbers()
        assert result == set()

    def test_is_nubers_valid(self, mocker):
        game = Game()
        input_mock = mocker.patch("Game.input")
        input_mock.return_value = "1"
        player_mock = mocker.patch("Game.Player")
        player_mock.get_name.return_value = "player"
        game.choose_config(configs, player_mock)
        result = game.is_numbers_valid({1,2,3})
        assert result == True
    
    def test_is_nubers_invalid(self, mocker):
        game = Game()
        input_mock = mocker.patch("Game.input")
        input_mock.return_value = "1"
        player_mock = mocker.patch("Game.Player")
        player_mock.get_name.return_value = "player"
        game.choose_config(configs, player_mock)
        result = game.is_numbers_valid({1,2,3,4,5})
        assert result == False
        result = game.is_numbers_valid({1,2})
        assert result == False
        result = game.is_numbers_valid({11,22,33})
        assert result == False
    
    def test_draw_numbers(self, mocker):
        game = Game()
        input_mock = mocker.patch("Game.input")
        input_mock.return_value = "1"
        player_mock = mocker.patch("Game.Player")
        player_mock.get_name.return_value = "player"
        game.choose_config(configs, player_mock)
        randint_mock = mocker.patch("Game.randint")
        randint_mock.side_effect = [1,2,2,2,2,2,3]
        result = game.draw_numbers()
        assert result == {1,2,3}
        
    def test_find_hit_numbers(self, mocker):
        game = Game()
        mocker.patch("Game.time")
        result = game.find_hit_numbers({1,2,3}, {1,2,3})
        assert result == {1,2,3}
        result = game.find_hit_numbers({6,4,8}, {1,2,3})
        assert result == set()
        result = game.find_hit_numbers({1,6,8}, {1,2,3})
        assert result == {1}

    def test_calculate_points(self, mocker):
        game = Game()
        input_mock = mocker.patch("Game.input")
        input_mock.return_value = "1"
        player_mock = mocker.patch("Game.Player")
        player_mock.get_name.return_value = "player"
        game.choose_config(configs, player_mock)
        result = game.calculate_points({1,2})
        assert result == 10
        result = game.calculate_points({})
        assert result == 0

    def test_play_again(self, mocker):
        game = Game()
        input_mock = mocker.patch("Game.input")
        input_mock.side_effect = ["Y", "N", ""]
        result = game.play_again()
        result == True
        result = game.play_again()
        result == False
        result = game.play_again()
        result == False
        