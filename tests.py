from main import *
import pytest


player = Player(name="player", level=1, playerPoints=0)
configs = [
        Config(1, 10, 3, "easy", 10),
        Config(1, 50, 5, "medium", 20),
        Config(1, 100, 8, "hard", 40)]


def test_get_name(mocker):
    input_mock = mocker.patch("main.input")
    input_mock.return_value = "kasia"
    result = get_name()
    assert result == "kasia"


def test_get_empty_name(mocker):
    input_mock = mocker.patch("main.input")
    input_mock.return_value = ""
    result = get_name()
    assert result == "player"


def test_choose_level(mocker):
    input_mock = mocker.patch("main.input")
    input_mock.return_value = "1"
    result = choose_level(player, configs)
    assert result == 1


def test_choose_negative_level(mocker):
    input_mock = mocker.patch("main.input")
    input_mock.return_value = "-1"
    result = choose_level(player, configs)
    assert result == -1


def test_choose_letter_level(mocker):
    input_mock = mocker.patch("main.input")
    input_mock.return_value = "a"
    result = choose_level(player, configs)
    assert result == -1


def test_is_level_correct():
    player.level = 1
    result = is_level_correct(configs, player)
    assert result == True


def test_is_level_incorrect_negative_value():
    player.level = -1
    result = is_level_correct(configs, player)
    assert result == False


def test_is_level_incorrect_number_higher_than_config():
    player.level = 4
    result = is_level_correct(configs, player)
    assert result == False


def test_get_numbers(mocker):
    input_mock = mocker.patch("main.input")
    input_mock.return_value = "1,2,3"
    result = get_numbers(configs[0])
    assert result == {1,2,3}


def test_get_numbers_with_wrong_data(mocker):
    input_mock = mocker.patch("main.input")
    input_mock.return_value = "a,b,c"
    result = get_numbers(configs[0])
    assert result == -1


def test_get_numbers_without_comma(mocker):
    input_mock = mocker.patch("main.input")
    input_mock.return_value = "1 * a B @ #"
    result = get_numbers(configs[0])
    assert result == -1


def test_validated_numbers():
    setSelectedNumbers = {1,2,3}
    result = validated_numbers(setSelectedNumbers, configs[0])
    assert result == True


def test_validated_numbers_higher_than_config():
    setSelectedNumbers = {1,2,3,4,5}
    result = validated_numbers(setSelectedNumbers, configs[0])
    assert result == False


def test_validated_numbers_lower_than_config():
    setSelectedNumbers = {1,2}
    result = validated_numbers(setSelectedNumbers, configs[0])
    assert result == False
