"""Module for calling the Crossmint API."""

from ratelimit import limits, sleep_and_retry
import constants
import requests


@sleep_and_retry
@limits(calls=1, period=1)
def _make_post_request(
        url: str,
        data: dict,
        timeout: float = constants.TIMEOUT_SECS):
    """Helper function to make a POST request."""
    return requests.post(url, data, timeout=timeout)


def call_polyanets_api(row: int, column: int):
    """Makes a HTTP request to create a Polyanet and returns the response."""
    return _make_post_request(
        constants.CROSSMINT_URL +
        constants.POLYANETS_API,
        {
            'candidateId': constants.CANDIDATE_ID,
            'row': row,
            'column': column})


def call_soloons_api(row: int, column: int, color: str):
    """Makes a HTTP request to create a Soloon and returns the response."""
    return _make_post_request(
        constants.CROSSMINT_URL +
        constants.SOLOONS_API,
        {
            'candidateId': constants.CANDIDATE_ID,
            'row': row,
            'column': column,
            'color': color})


def call_comeths_api(row: int, column: int, direction: str):
    """Makes a HTTP request to create a Cometh and returns the response."""
    return _make_post_request(
        constants.CROSSMINT_URL +
        constants.COMETH_API,
        {
            'candidateId': constants.CANDIDATE_ID,
            'row': row,
            'column': column,
            'direction': direction})
