from Player import Player
from Game import Game
from main import *
import pytest


configs = [
        Config(1, 10, 3, "easy", 5),
        Config(1, 50, 5, "medium", 10),
        Config(1, 100, 8, "hard", 15)]


@pytest.fixture
def player_input(mocker):
    input_mock = mocker.patch("Player.input")
    return input_mock


@pytest.fixture
def game_input(mocker):
    input_mock = mocker.patch("Game.input")
    return input_mock


@pytest.fixture
def player_mock(mocker):
    player = mocker.patch("Game.Player")
    return player


@pytest.fixture
def randint_mock(mocker):
    randint = mocker.patch("Game.randint")
    return randint


@pytest.fixture
def player_time(mocker):
    time = mocker.patch("Player.time")
    return time


@pytest.fixture
def game_time(mocker):
    time = mocker.patch("Game.time")
    return time


class TestPlayer:

    def test_create_player_object(self, player_input):
        player_input.return_value = "asd"

        Player()
        
    @pytest.mark.parametrize("test_input,expected", [("tomek", "tomek"), ("", "player")])
    def test_input__name(self, player_input, test_input, expected):
        player_input.return_value = test_input

        player = Player()

        assert player.get_name() == expected

    def test_add_points(self, player_input, player_time):
        player_input.return_value = ""

        player = Player()

        result = player.add_points(5)
        assert result == 5
        result = player.add_points(0)
        assert result == 5
        result = player.add_points(3)
        assert result == 8

class TestGame:

    def test_create_game_object(self):
        Game()
    
    @pytest.mark.parametrize("test_input, expected", [("w", -1), ("", -1), ("1", 0)])
    def test_get_config_from_user(self, game_input, test_input, expected):
        game_input.return_value = test_input

        game = Game()

        assert game.get_config_from_user() == expected
        
    @pytest.mark.parametrize("test_input, expected", [(["1"], 1), (["4", "2"], 2)])
    def test_choose_config(self, game_input, player_mock, test_input, expected):
        game_input.side_effect = test_input
        player_mock.get_name.return_value = "player"

        game = Game()
        game.choose_config(configs, player_mock)

        assert player_mock.get_name.call_count == expected
 
    @pytest.mark.parametrize("test_input, expected", [
        (["1", "1,2,3"], {1,2,3}),
        (["1", "a,b,.", "3,2,5"], {3,2,5})
    ])
    def test_get_numbers(self, game_input, player_mock, test_input, expected):
        game_input.side_effect = test_input
        player_mock.get_name.return_value = "player"

        game = Game()
        game.choose_config(configs, player_mock)

        assert game.get_numbers() == expected

    @pytest.mark.parametrize("numbers, expected", [
        ({1,2,3}, True),
        ({1,2,3,4,5}, False),
        ({1,2}, False),
        ({11,22,33}, False)
    ])
    def test_is_numbers_valid(self, game_input, player_mock, numbers, expected):
        game_input.return_value = "1"
        player_mock.get_name.return_value = "player"

        game = Game()
        game.choose_config(configs, player_mock)

        assert game.is_numbers_valid(numbers) == expected
    
    def test_draw_numbers(self, game_input, player_mock, randint_mock):
        game_input.return_value = "1"
        player_mock.get_name.return_value = "player"
        randint_mock.side_effect = [1,2,2,2,2,2,3]

        game = Game()
        game.choose_config(configs, player_mock)
        
        result = game.draw_numbers()
        assert result == {1,2,3}
    
    @pytest.mark.parametrize("choose_numbers, drawn_numbers, hit_numbers", [
        ({1,2,3}, {1,2,3}, {1,2,3}),
        ({6,4,8},{1,2,3}, set()),
        ({1,6,8}, {1,2,3}, {1})
    ])
    def test_find_hit_numbers(self, game_time, choose_numbers, drawn_numbers, hit_numbers):
        game = Game()

        assert game.find_hit_numbers(choose_numbers, drawn_numbers) == hit_numbers

    @pytest.mark.parametrize("hit_numbers, points", [({1,2}, 10), ({}, 0)])
    def test_calculate_points(self, game_input, player_mock, hit_numbers, points):
        game_input.return_value = "1"
        player_mock.get_name.return_value = "player"

        game = Game()
        game.choose_config(configs, player_mock)

        assert game.calculate_points(hit_numbers) == points

    def test_play_again(self, game_input):
        game_input.side_effect = ["Y", "N", ""]

        game = Game()

        result = game.play_again()
        result == True
        result = game.play_again()
        result == False
        result = game.play_again()
        result == False
        