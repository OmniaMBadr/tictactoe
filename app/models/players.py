from dataclasses import dataclass, field    

from app.services import RandomChoiceService


@dataclass
class Player:
    identifier: str
    positions: list[int] = field(init=False)

    def __post_init__(self):
        self.positions = []

    def __str__(self):
        return f"Player: {self.identifier}"

    @staticmethod
    def play(avaiable_positions: list[int]) -> int:
        return RandomChoiceService.get_choice(avaiable_positions)

    def add_position(self, position: int) -> None:
        self.positions.append(position)

    def get_positions(self):
        return self.positions
