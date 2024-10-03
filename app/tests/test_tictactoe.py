import unittest

from app.models.tictactoe import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def test_creation(self):
        tictactoe = TicTacToe()
        self.assertIsNotNone(tictactoe.BOARD_DIMENSION)
        self.assertIsNotNone(tictactoe.board)
        self.assertEqual(len(tictactoe.players), 2)
        self.assertEqual(tictactoe.next_player_index, 0)
