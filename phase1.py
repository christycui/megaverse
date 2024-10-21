import api_helpers
import constants
import square


SQUARE_SIZE = 11


def generate_polyanet_cross(shape: square.Square):
	"""Generates a polyanet cross."""
	polyanets = shape.get_cross()
	success = True
	for polyanet in polyanets:
		response = api_helpers.call_polyanets_api(polyanet.row, polyanet.column)
		if response.status_code != requests.codes.ok:
			print('Failed to generate polynet! Status code is:', response.status_code)
			success = False
			break
	if success:
		print('Success! Created a polyanets cross!')

def main():
	square = square.Square(SQUARE_SIZE)
	generate_polyanet_cross(square)

if __name__ == "__main__":
    main()