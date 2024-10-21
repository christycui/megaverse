"""Phase 1 solution runner."""

import api_helpers
import requests
from megaverse import Megaverse


SQUARE_SIZE = 11


def generate_polyanet_cross(megaverse: Megaverse):
    """Generates a polyanet cross."""
    polyanets = megaverse.get_cross()
    success = True
    for polyanet in polyanets:
        response = api_helpers.call_polyanets_api(
            polyanet.row, polyanet.column)
        if response.status_code != requests.codes.ok:
            print(
                'Failed to generate polynet! Status code is:',
                response.status_code)
            success = False
            break
    if success:
        print('Success! Created a polyanets cross!')


def main():
    """Main program."""
    megaverse_phase1 = Megaverse(SQUARE_SIZE)
    generate_polyanet_cross(megaverse_phase1)


if __name__ == "__main__":
    main()
