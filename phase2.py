from enum import Enum
from entities import Cometh, Polyanet, Soloon, Color, Direction
from ratelimit import limits, sleep_and_retry
import api_helpers
import requests
from square import Square


SQUARE_SIZE = 30

def _format_enum(enum) -> str:
	"""Formats the enum values into lowercase."""
	return enum.name.lower()


def generate_crossmint(shape: Square):
	"""Generates a crossmint."""
	crossmint_entities = shape.get_crossmint()
	success = True
	for entity in crossmint_entities:
		response = None
		if entity.__class__ == Polyanet:
			response = api_helpers.call_polyanets_api(entity.row, entity.column)
		if entity.__class__ == Soloon:
			response = api_helpers.call_soloons_api(entity.row, entity.column, _format_enum(entity.color))
		if entity.__class__ == Cometh:
			response = api_helpers.call_comeths_api(entity.row, entity.column, _format_enum(entity.direction))
		if response and response.status_code != requests.codes.ok:
			print('Failed to generate entity! Status code is:', response.status_code)
			success = False
			break
	if success:
		print('Success! Created a crossmint!')


def main():
	square = Square(SQUARE_SIZE)
	generate_crossmint(square)

if __name__ == "__main__":
    main()