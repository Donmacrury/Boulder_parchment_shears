import unittest
from app.models.game import *
from app.models.player import *

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game("Player 1 Wins!")
        self.player_1 = Player("player 1", "rock ")
        self.player_2 = Player("player 2", "scissors")

    def test_game_has_outcome(self):
        self.assertEqual("Player 1 Wins!", self.game.outcome)

    def test_game_has_a_player(self):
        self.game.add_player(self.player_1)
        self.assertEqual(1, self.game.current_player())

    def test_game_has_only_two_players(self):
        self.game.add_player(self.player_1)
        self.game.add_player(self.player_1)
        self.game.add_player(self.player_1)
        self.assertEqual(2, self.game.current_player())
    
    def test_get_choices_returns_players_choices(self):
        self.game.add_player(self.player_1)
        self.game.add_player(self.player_2)
        self.assertEqual("rock scissors", self.game.get_players_choices()) 

    def test_assert_player_1_win_if_paper_v_rock(self):
        new_game = Game("")
        player_1 = Player("player_1", "paper ")
        player_2 = Player("player_2", "rock")        
        new_game.add_player(player_1)
        new_game.add_player(player_2)
        new_game.compare_choices()
        self.assertEqual("Player 1 Wins!", new_game.outcome)

    def test_assert_player_2_win_if_paper_v_scissors(self):
        new_game = Game("")
        player_1 = Player("player_1", "paper ")
        player_2 = Player("player_2", "scissors")        
        new_game.add_player(player_1)
        new_game.add_player(player_2)
        new_game.compare_choices()
        self.assertEqual("Player 2 Wins!", new_game.outcome)

    def test_assert_draw_if_paper_v_paper(self):
        new_game = Game("")
        player_1 = Player("player_1", "paper ")
        player_2 = Player("player_2", "paper")        
        new_game.add_player(player_1)
        new_game.add_player(player_2)
        new_game.compare_choices()
        self.assertEqual("A Draw!", new_game.outcome)
