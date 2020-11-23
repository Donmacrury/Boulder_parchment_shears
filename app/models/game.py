class Game:

    def __init__(self, outcome):
        self.outcome = outcome
        self.players = []

    def current_player(self):
        return len(self.players)

    def add_player(self, new_player):
        if self.current_player() < 2:
            self.players.append(new_player)

    def get_players_choices(self):
        choices = ""
        for player in self.players:
            choices += player.choice
        return choices         

    def compare_choices(self):
        if self.get_players_choices() == "rock scissors":
            self.outcome = "Player 1 Wins!"
        if self.get_players_choices() == "scissors paper":
            self.outcome = "Player 1 Wins!"
        if self.get_players_choices() == "paper rock":
            self.outcome = "Player 1 Wins!"
        if self.get_players_choices() == "paper scissors":
            self.outcome = "Player 2 Wins!"
        if self.get_players_choices() == "rock paper":
            self.outcome = "Player 2 Wins!"
        if self.get_players_choices() == "scissors rock":
            self.outcome = "Player 2 Wins!"
        if self.get_players_choices() == "paper paper":
            self.outcome = "A Draw!"
        if self.get_players_choices() == "rock rock":
            self.outcome = "A Draw!"
        if self.get_players_choices() == "scissors scissors":
            self.outcome = "A Draw!"