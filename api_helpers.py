from ratelimit import limits, sleep_and_retry
import constants
import requests


@sleep_and_retry
@limits(calls=1, period=1)
def call_polyanets_api(row: int, column: int):
	"""Makes a HTTP request to create a Polyanet and returns the response."""
	return requests.post(
			constants.CROSSMINT_URL+constants.POLYANETS_API,
			data={'candidateId': constants.CANDIDATE_ID, 'row': row, 'column': column})


@sleep_and_retry
@limits(calls=1, period=1)
def call_soloons_api(row: int, column: int, color: str):
	"""Makes a HTTP request to create a Soloon and returns the response."""
	return requests.post(
			constants.CROSSMINT_URL+constants.SOLOONS_API,
			data={'candidateId': constants.CANDIDATE_ID, 'row': row, 'column': column, 'color': color})


@sleep_and_retry
@limits(calls=1, period=1)
def call_comeths_api(row: int, column: int, direction: str):
	"""Makes a HTTP request to create a Cometh and returns the response."""
	return requests.post(
			constants.CROSSMINT_URL+constants.COMETH_API,
			data={'candidateId': constants.CANDIDATE_ID, 'row': row, 'column': column, 'direction': direction})
