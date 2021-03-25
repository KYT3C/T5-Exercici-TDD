class Game:
    def __init__(self, player1: str, player2: str):
        self._player1 = player1
        self._player2 = player2
        self._player2Points = 0
        self._player1Points = 0
        self._wins = ""

    def wins_point(self, player: str, score):
        if player == self._player1:
            self._player1Points = score
        else:
            self._player2Points = score

    def get_score(self) -> str:
        if (self._player1Points == 0) & (self._player2Points == 0):
            return "Love-All"
        if (self._player1Points == 1) & (self._player2Points == 1):
            return "Fifteen-All"
        if (self._player1Points == 2) & (self._player2Points == 2):
            return "Thirty-All"
