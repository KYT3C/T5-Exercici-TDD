class Game:
    def __init__(self, player1: str, player2: str):
        self._player1 = player1
        self._player2 = player2
        self._player2Points = 0
        self._player1Points = 0
        self._wins = ""

    def wins_point(self, player: str):
        if  player == self._player1:
            self._player1Points += 1
        else:
            self._player2Points += 1

    def get_score(self) -> str:
        if (self._player1Points == 0) & (self._player2Points == 0):
            return "Love-All"
        if (self._player1Points == 1) & (self._player2Points == 1):
            return "Fifteen-All"
