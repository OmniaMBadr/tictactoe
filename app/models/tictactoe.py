from dataclasses import dataclass, field    

from app.models.boards import Board
from app.models.players import Player


class TicTacToe:

    BOARD_DIMENSION: int = 3
    board: Board = field(init=False)
    players: list[Player] = field(init=False)
    next_player_index: int = field(init=False)

    def __init__(self):
        self.board = Board(self.BOARD_DIMENSION)
        self.players = [Player("X"), Player("O")]
        self.next_player_index = 0

    def play(self) -> Player:
        player = self.get_next_player()
        position = player.play(self.board.get_avaiable_positions())
        if self.board.set_player_position(position, player.identifier):
            player.add_position(position)
            self.set_next_player()
        else:
            raise Exception("TicTacToe: Invalid position {position} by {player}")
        if self.board.is_player_winner(player):
            return player
        if self.check_game_over():
            return Player("No one")

    def get_next_player(self) -> Player:
        return self.players[self.next_player_index]

    def set_next_player(self) -> None:
        self.next_player_index = int(not self.next_player_index)

    def check_game_over(self) -> bool:
        return not self.board.has_avaiable_positions()
