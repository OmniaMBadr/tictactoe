from dataclasses import dataclass, field    

from app.models.players import Player


@dataclass
class Board:
    dimension: int
    avaiable_positions: list[int] = field(init=False)
    value: list[str] = field(init=False)
    winning_positions: list[set] = field(init=False)


    def __post_init__(self):
        self.avaiable_positions = list(range(self.dimension ** 2))
        self.value = ["-"] * self.dimension ** 2
        self.set_winning_positions()

    def __str__(self) -> str:
        str_value = " "
        for i in range(self.dimension):
            str_value += " | ".join(self.value[i * self.dimension: i * self.dimension + self.dimension])
            str_value += " \n "

        return str_value

    def set_winning_positions(self):
        self.winning_positions = []

        row_positions = [list() for i in range(self.dimension)]
        column_positions = [list() for i in range(self.dimension)]
        diagonal = []
        secondary_diagonal= []
                
        for position in self.avaiable_positions:
            position_row = int(position / self.dimension)
            position_coloumn = position % self.dimension
            row_positions[position_row].append(position)
            column_positions[position_coloumn].append(position)

            if position_row == position_coloumn:
                diagonal.append(position)
            if position_row + position_coloumn + 1 == self.dimension:
                secondary_diagonal.append(position)

        for winning_position in row_positions + column_positions + [diagonal] + [secondary_diagonal]:
            self.winning_positions.append(set(winning_position))

    def get_avaiable_positions(self) -> list[int]:
        return self.avaiable_positions

    def has_avaiable_positions(self) -> bool:
        return bool(self.avaiable_positions)

    def set_player_position(self, position: int, identifier: str) -> bool:
        if position not in self.avaiable_positions:
            return False
        self.avaiable_positions.remove(position)
        self.value[position] = identifier
        return True

    def is_player_winner(self, player: Player) -> bool:
        for winning_position in self.winning_positions:
            if winning_position.issubset(player.get_positions()):
                return True
        return False
