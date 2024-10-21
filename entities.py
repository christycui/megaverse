from enum import Enum


Color = Enum('Color', ['BLUE', 'RED', 'PURPLE', 'WHITE'])
Direction = Enum('Direction', ['UP', 'DOWN', 'LEFT', 'RIGHT'])


class AstralObject():
	"""Base class representing an astral object."""
	def __init__(self, row: int, column: int):
		self.row = row
		self.column = column


class Polyanet(AstralObject):
	def __init__(self, row: int, column: int):
		AstralObject.__init__(self, row, column)

class Soloon(AstralObject):
	def __init__(self, row: int, column: int, color: Color):
		self.color = color
		AstralObject.__init__(self, row, column)


class Cometh(AstralObject):
	def __init__(self, row: int, column: int, direction: Direction):
		self.direction = direction
		AstralObject.__init__(self, row, column)