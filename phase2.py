"""Phase 2 solution runner."""

from entities import Cometh, Polyanet, Soloon
import api_helpers
from megaverse import Megaverse
import requests


SQUARE_SIZE = 30


def _format_enum(enum) -> str:
    """Formats the enum values into lowercase."""
    return enum.name.lower()


def generate_crossmint(megaverse: Megaverse):
    """Generates a crossmint."""
    crossmint_entities = megaverse.get_crossmint()
    success = True
    for entity in crossmint_entities:
        response = None
        if entity.__class__ == Polyanet:
            response = api_helpers.call_polyanets_api(
                entity.row, entity.column)
        if entity.__class__ == Soloon:
            response = api_helpers.call_soloons_api(
                entity.row, entity.column, _format_enum(entity.color))
        if entity.__class__ == Cometh:
            response = api_helpers.call_comeths_api(
                entity.row, entity.column, _format_enum(entity.direction))
        if response and response.status_code != requests.codes.ok:
            print(
                'Failed to generate entity! Status code is:',
                response.status_code)
            success = False
            break
    if success:
        print('Success! Created a crossmint!')


def main():
    """Main program."""
    megaverse_phase2 = Megaverse(SQUARE_SIZE)
    generate_crossmint(megaverse_phase2)


if __name__ == "__main__":
    main()
