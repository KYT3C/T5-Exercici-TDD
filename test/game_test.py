import unittest
import sys

sys.path.append('../')

from main.Game import Game


class MyTestCase(unittest.TestCase):

    def test_gameStart(self):
        game = Game("Gonzalo", "Ismael")
        result = game.get_score()
        assert result == "Love-All"


if __name__ == '__main__':
    unittest.main()
