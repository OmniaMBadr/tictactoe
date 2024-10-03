from app.models.boards import Board

import unittest

from app.models.players import Player


class TestBoard(unittest.TestCase):

    def test_creation(self):
        dimension = 5

        board = Board(dimension=dimension)
        self.assertEqual(board.avaiable_positions, list(range(dimension ** 2)))
        self.assertEqual(board.value, ["-"] * dimension ** 2)
        self.assertEqual(len(board.winning_positions), dimension * 2 + 2)

    def test_board_dimension_is_required_at_creation(self):
        with self.assertRaises(TypeError) as error:
            Board()
        self.assertEqual(str(error.exception), "__init__() missing 1 required positional argument: 'dimension'")

    def test_serialization(self):
        board = Board(3)
        board.value = ["X", "O", "O", "-", "X", "O", "-", "X", "X"]
        self.assertEqual(str(board), " X | O | O \n - | X | O \n - | X | X \n ")

    def test_set_winning_positions(self):
        dimension = 5
        board = Board(5)
        winning_positions = [
            {0, 1, 2, 3, 4}, {5, 6, 7, 8, 9}, {10, 11, 12, 13, 14}, {15, 16, 17, 18, 19}, {20, 21, 22, 23, 24},
            {0, 5, 10, 15, 20}, {1, 6, 11, 16, 21}, {2, 7, 12, 17, 22}, {3, 8, 13, 18, 23}, {4, 9, 14, 19, 24},
            {0, 6, 12, 18, 24}, {4, 8, 12, 16, 20}
            ]
        self.assertEqual(winning_positions, board.winning_positions)

    def test_set_player_empty_position_successfully(self):
        position=3
        identifier="R"
        board = Board(3)
        self.assertIn(position, board.avaiable_positions)
        self.assertNotEqual(board.value[position], identifier)

        self.assertTrue(board.set_player_position(position=position, identifier=identifier))
        self.assertNotIn(position, board.avaiable_positions)
        self.assertEqual(board.value[position], identifier)

    def test_set_player_occupied_position_failure(self):
        position=3
        identifier="R"
        other_identifier = "O"
        board = Board(3)
        board.set_player_position(position=position, identifier=other_identifier)

        self.assertFalse(board.set_player_position(position=position, identifier=identifier))
        self.assertNotIn(position, board.avaiable_positions)
        self.assertEqual(board.value[position], other_identifier)

    def test_is_player_winner_for_winner(self):
        board = Board(3)
        player = Player("P")
        player.positions = list(board.winning_positions[1])
        self.assertTrue(board.is_player_winner(player))

    def test_is_player_winner_for_not_winner(self):
        board = Board(3)
        player = Player("P")
        player.positions = []
        self.assertFalse(board.is_player_winner(player))
