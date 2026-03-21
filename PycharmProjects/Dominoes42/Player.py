# Player Base Class
class Player:
    def __init__(self, name, team, bid):
        self.name = name
        self.team = team
        self.hand = []
        self.bid = None

    def receive_domino(self, domino):
        self.hand.append(domino)

    def __str__(self):
        return f"{self.name} (Team {self.team}): {len(self.hand)} dominos"

    def get_bid(self, current_high_bid):
        pass

# HumanPlayer Class (inherits from Player)
class HumanPlayer(Player):
    def __init__(self, name, team, bid):
        super().__init__(name, team, bid)
        self.is_human = True
        self.needs_input = True  # Needs to wait for button clicks
        self.show_hand_visual = True  # Display dominos visually


# AIPlayer Class (inherits from Player)
class AIPlayer(Player):
    def __init__(self, name, team, bid):
        super().__init__(name, team, bid)
        self.is_human = False
        self.needs_input = False  # Auto-plays
        self.show_hand_visual = False  # No need to display AI hands