from typing import List, Tuple
from entities import AstralObject, Color, Cometh, Direction, Polyanet, Soloon


CROSSMINT_CENTER = 13
CROSSMINT_MIN_SIZE = 30


class Square():
	def __init__(self, side: int):
		self.side = side
		self._validate()
		self.map = [[None]*side]*side

	def get_cross(self, padding: int = 2) -> List[Polyanet]:
		"""Returns a list of Polynets that create a cross."""
		# The smallest cross is 3x3 (1x1 is a dot and not considered a square).
		if self.side < 2 * padding + 3:
			raise ValueError('Square is not large enough to generate a cross with a padding of', padding)

		mid = self.side // 2
		positions = [(mid, mid)] # Middle of the cross.
		for i in range(1, self.side - mid - padding):
			positions.append(Polyanet(mid-i, mid-i))
			positions.append(Polyanet(mid+i, mid+i))
			positions.append(Polyanet(mid-i, mid+i))
			positions.append(Polyanet(mid+i, mid-i))
		self._update_map(positions)
		return positions

	def get_crossmint(self) -> List[AstralObject]:
		"""Returns a list of AstralObjects that create a crossmint."""
		if self.side < CROSSMINT_MIN_SIZE:
			raise ValueError('Square is not large enough to generate a crossmint.')

		entities = []
		entities.extend(self._add_crossmint_polyanets())
		entities.extend(self._add_crossmint_soloons())
		entities.extend(self._add_crossmint_comeths())
		return entities

	def _add_crossmint_polyanets(self) -> List[Polyanet]:
		"""Returns a list of Polyanets that are part of the crossmint."""
		polyanets = []
		offsets = [(0, 0), (-1, 0), (-2, 1), (-3, 1), (-4, 2), (-5, 2), (-6, 3), (-7, 3), (-8, 4), (-8, 5), (-9, 6), (-9, 7), (-10, 8), (-10, 9), (-11, 10), (-11, 11)]
		for offset_x, offset_y in offsets:
			polyanets.append(Polyanet(row=CROSSMINT_CENTER+offset_x, column=CROSSMINT_CENTER+offset_y))
			polyanets.append(Polyanet(row=CROSSMINT_CENTER-offset_x, column=CROSSMINT_CENTER+offset_y))
			polyanets.append(Polyanet(row=CROSSMINT_CENTER+offset_x, column=CROSSMINT_CENTER-offset_y))
			polyanets.append(Polyanet(row=CROSSMINT_CENTER-offset_x, column=CROSSMINT_CENTER-offset_y))
			polyanets.append(Polyanet(row=CROSSMINT_CENTER+offset_y, column=CROSSMINT_CENTER+offset_x))
			polyanets.append(Polyanet(row=CROSSMINT_CENTER-offset_y, column=CROSSMINT_CENTER+offset_x))
			polyanets.append(Polyanet(row=CROSSMINT_CENTER+offset_y, column=CROSSMINT_CENTER-offset_x))
			polyanets.append(Polyanet(row=CROSSMINT_CENTER-offset_y, column=CROSSMINT_CENTER-offset_x))
		self._update_map(polyanets)
		return polyanets


	def _add_crossmint_soloons(self) -> List[Soloon]:
		"""Returns a list of Soloons that are part of the crossmint."""
		soloons = [Soloon(3, 20, Color.WHITE), Soloon(4, 5, Color.BLUE), Soloon(4, 8, Color.PURPLE),
			Soloon(5, 6, Color.WHITE), Soloon(5, 20, Color.BLUE), Soloon(7, 15, Color.RED),
			Soloon(7, 23, Color.PURPLE), Soloon(8, 4, Color.WHITE), Soloon(8, 10, Color.BLUE),
			Soloon(9, 6, Color.PURPLE), Soloon(9, 12, Color.RED), Soloon(10, 18, Color.PURPLE),
			Soloon(11, 7, Color.BLUE), Soloon(14, 9, Color.WHITE), Soloon(14, 17, Color.BLUE),
			Soloon(15, 19, Color.WHITE), Soloon(16, 8, Color.BLUE), Soloon(16, 21, Color.BLUE),
			Soloon(17, 14, Color.PURPLE), Soloon(18, 6, Color.PURPLE), Soloon(18, 22, Color.RED),
			Soloon(19, 11, Color.WHITE), Soloon(21, 10, Color.RED), Soloon(21, 16, Color.WHITE),
			Soloon(21, 19, Color.PURPLE), Soloon(22, 5, Color.RED), Soloon(22, 8, Color.BLUE),
			Soloon(22, 24, Color.RED)]
		for soloon in soloons:
			if not self._has_polyanet_neighbor(soloon):
				raise ValueError('Soloon must be next to a Polyanet.')
		self._update_map(soloons)
		return soloons


	def _has_polyanet_neighbor(self, entity: AstralObject) -> bool:
		"""Return a boolean value representing whether entity has a Polyanet neighbor."""
		row, column = entity.row, entity.column
		neighbors = [(row-1, column-1), (row-1, column+1), (row+1, column-1), (row+1, column+1)]
		found = False
		for x, y in neighbors:
			if isinstance(self.map[x % self.side][y % self.side], Polyanet):
				found = True
		return found


	def _add_crossmint_comeths(self) -> List[Cometh]:
		"""Returns a list of Comeths that are part of the crossmint."""
		comeths = [Cometh(1, 7, Direction.RIGHT), Cometh(2, 13, Direction.UP), Cometh(3, 27, Direction.LEFT),
		Cometh(4, 16, Direction.LEFT), Cometh(4, 29, Direction.RIGHT), Cometh(5, 12, Direction.DOWN),
		Cometh(9, 27, Direction.UP), Cometh(10, 2, Direction.UP), Cometh(12, 25, Direction.LEFT),
		Cometh(12, 28, Direction.DOWN), Cometh(13, 4, Direction.RIGHT), Cometh(15, 1, Direction.LEFT),
		Cometh(15, 26, Direction.RIGHT), Cometh(16, 3, Direction.DOWN), Cometh(17, 24, Direction.UP),
		Cometh(20, 0, Direction.RIGHT), Cometh(22, 14, Direction.LEFT), Cometh(22, 27, Direction.DOWN),
		Cometh(24, 12, Direction.UP), Cometh(26, 3, Direction.DOWN), Cometh(26, 15, Direction.DOWN),
		Cometh(26, 26, Direction.UP), Cometh(27, 5, Direction.LEFT), Cometh(28, 10, Direction.RIGHT),
		Cometh(28, 20, Direction.LEFT)]
		self._update_map(comeths)
		return comeths


	def _validate(self):
		"""Raises a ValueError if side is not positive; otherwise, returns None."""
		if self.side <= 0:
			raise ValueError('The side of the square must be greater than zero.')


	def _update_map(self, entities: List[AstralObject]):
		"""Updates the map with a list of AstralObjects."""
		for entity in entities:
			self.map[entity.row][entity.column] = entity