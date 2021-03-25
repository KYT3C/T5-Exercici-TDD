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
        if (self._player1Points >= 3) & (self._player2Points >= 3) & (self._player1Points == self._player2Points):
            return "Deuce"
        if self._player1Points == 0:
            if self._player2Points == 1:
                return "Love-Fifteen"
            if self._player2Points == 2:
                return "Love-Thirty"
            if self._player2Points == 3:
                return "Love-Forty"
        if self._player2Points == 0:
            if self._player1Points == 1:
                return "Fifteen-Love"
            if self._player1Points == 2:
                return "Thirty-Love"
            if self._player1Points == 3:
                return "Forty-Love"
        if (self._player1Points == 4) & (self._player2Points < 3):
            return "Win for player1"
        if (self._player2Points == 4) & (self._player1Points < 3):
            return "Win for player2"
        if (self._player1Points > 4) & ((self._player1Points - self._player2Points) == 2):
            return "Win for player1"
        if (self._player2Points > 4) & ((self._player2Points - self._player1Points) == 2):
            return "Win for player2"
        if (self._player1Points == 1):
            if (self._player2Points == 2):
                return "Fifteen-Thirty"
            if (self._player2Points == 3):
                return "Fifteen-Forty"
        if (self._player2Points == 1):
            if (self._player1Points == 2):
                return "Thirty-Fifteen"
            if (self._player1Points == 3):
                return "Forty-Fifteen"
