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

    def test_player1_Love_Something(self):
        game = gameSetUp()
        game.wins_point("Gonzalo", 0)
        game.wins_point("Ismael", 1)
        result = game.get_score()
        assert result == "Love-Fifteen"

        game = gameSetUp()
        game.wins_point("Gonzalo", 0)
        game.wins_point("Ismael", 2)
        result = game.get_score()
        assert result == "Love-Thirty"

        game = gameSetUp()
        game.wins_point("Gonzalo", 0)
        game.wins_point("Ismael", 3)
        result = game.get_score()
        assert result == "Love-Forty"

    def test_player1_Something_Love(self):
        game = gameSetUp()
        game.wins_point("Gonzalo", 1)
        game.wins_point("Ismael", 0)
        result = game.get_score()
        assert result == "Fifteen-Love"

        game = gameSetUp()
        game.wins_point("Gonzalo", 2)
        game.wins_point("Ismael", 0)
        result = game.get_score()
        assert result == "Thirty-Love"

        game = gameSetUp()
        game.wins_point("Gonzalo", 3)
        game.wins_point("Ismael", 0)
        result = game.get_score()
        assert result == "Forty-Love"

    def test_player1Win(self):
        game = gameSetUp()
        game.wins_point("Gonzalo", 4)
        game.wins_point("Ismael", 0)
        result = game.get_score()
        assert result == "Win for player1"

        game = gameSetUp()
        game.wins_point("Gonzalo", 6)
        game.wins_point("Ismael", 4)
        result = game.get_score()
        assert result == "Win for player1"

        game = gameSetUp()
        game.wins_point("Gonzalo", 16)
        game.wins_point("Ismael", 14)
        result = game.get_score()
        assert result == "Win for player1"

    def test_player2Win(self):
        game = gameSetUp()
        game.wins_point("Gonzalo", 0)
        game.wins_point("Ismael", 4)
        result = game.get_score()
        assert result == "Win for player2"

        game = gameSetUp()
        game.wins_point("Gonzalo", 4)
        game.wins_point("Ismael", 6)
        result = game.get_score()
        assert result == "Win for player2"

        game = gameSetUp()
        game.wins_point("Gonzalo", 14)
        game.wins_point("Ismael", 16)
        result = game.get_score()
        assert result == "Win for player2"

if __name__ == '__main__':
    unittest.main()
