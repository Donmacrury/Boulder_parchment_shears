import unittest
from app.models.player import *

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Player 1", "rock")

    def test_player_has_name(self):
        self.assertEqual("Player 1", self.player.name)

    def test_player_has_choice(self):
        self.assertEqual("rock", self.player.choice)