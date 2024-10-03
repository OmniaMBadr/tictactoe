import unittest

from app.models.players import Player


class TestPlayer(unittest.TestCase):

    def test_creation(self):
        identifier = "Player"
        player = Player(identifier)

        self.assertEqual(player.identifier, identifier)
        self.assertEqual(player.positions, [])

    def test_player_identifier_is_required_at_creation(self):
        with self.assertRaises(TypeError) as error:
            Player()
        self.assertEqual(str(error.exception), "__init__() missing 1 required positional argument: 'identifier'")

    def test__serialization(self):
        identifier = "Player"
        player = Player(identifier)
        self.assertEqual(str(player), f"Player: {player.identifier}")

    def test_add_position(self):
        player = Player("")
        position = 3
        self.assertNotIn(position, player.get_positions())
        player.add_position(position)
        self.assertIn(position, player.get_positions())
