# Player Base Class
class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.hand = []
        self.bid = None

    def needs_input(self):  # Abstract method - must be overridden in derived classes
        raise NotImplementedError

    def receive_domino(self, domino):
        self.hand.append(domino)

    def __str__(self):
        return f"{self.name} (Team {self.team}): {len(self.hand)} dominos"

# HumanPlayer Class (inherits from Player)
class HumanPlayer(Player):
    def __init__(self, name, team, is_local=False):
        super().__init__(name, team)
        self.is_human = True
        self.needs_input = True  # Needs to wait for button clicks
        self.is_local = is_local  # Only Human players can be "local"

    def needs_input(self):
        return True

# AIPlayer Class (inherits from Player)
class AIPlayer(Player):
    def __init__(self, name, team):
        super().__init__(name, team)
        self.is_human = False
        self.needs_input = False  # Auto-plays



