"""Module defining astral entities."""

from enum import Enum
import dataclasses


Color = Enum('Color', ['BLUE', 'RED', 'PURPLE', 'WHITE'])
Direction = Enum('Direction', ['UP', 'DOWN', 'LEFT', 'RIGHT'])


@dataclasses.dataclass
class AstralObject():
    """Base class representing astral entities."""
    row: int
    column: int


@dataclasses.dataclass
class Polyanet(AstralObject):
    """Class for Polyanets."""


@dataclasses.dataclass
class Soloon(AstralObject):
    """Class for Soloons."""
    color: Color


@dataclasses.dataclass
class Cometh(AstralObject):
    """Class for Comeths."""
    direction: Direction
