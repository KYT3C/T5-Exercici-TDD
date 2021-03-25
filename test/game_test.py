import unittest
import sys

sys.path.append('../')

from main.Game import Game

def gameSetUp() -> Game:
    return Game("Gonzalo", "Ismael")

class MyTestCase(unittest.TestCase):

    def test_gameStart(self):
        game = gameSetUp()
        result = game.get_score()
        assert result == "Love-All"

    def test_FifteenAll(self):
        game = gameSetUp()
        game.wins_point("Gonzalo", 1)
        game.wins_point("Ismael", 1)
        result = game.get_score()
        assert result == "Fifteen-All"

    def test_Thirty_All(self):
        game = gameSetUp()
        game.wins_point("Gonzalo", 2)
        game.wins_point("Ismael", 2)
        result = game.get_score()
        assert result == "Thirty-All"

    def test_Deuce(self):
        game = gameSetUp()
        game.wins_point("Gonzalo", 3)
        game.wins_point("Ismael", 3)
        result = game.get_score()
        assert result == "Deuce"

        game.wins_point("Gonzalo", 8)
        game.wins_point("Ismael", 8)
        result = game.get_score()
        assert result == "Deuce"



if __name__ == '__main__':
    unittest.main()
