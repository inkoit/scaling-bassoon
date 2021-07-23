"""Client for the Wikipedia REST API, version 1."""

import click
import pydantic
import requests

API_URL = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"


class Page(pydantic.BaseModel):
    """Page resource.

    Attributes:
        title: The title of the Wikipedia page.
        extract: A plain text summary.
    """

    title: str
    extract: str


def random_page(language: str = "en") -> Page:
    """Return a random page.

    Performs a GET request to the /page/random/summary endpoint.

    Args:
        language: The Wikipedia language edition. By default, the English
            Wikipedia is used ("en").

    Returns:
        A page resource.

    Raises:
        ClickException: The HTTP request failed or the HTTP response
            contained an invalid body.

    Example:
        >>> from scaling_bassoon import wikipedia
        >>> page = wikipedia.random_page(language="en")
        >>> bool(page.title)
        True
    """
    try:
        with requests.get(API_URL.format(language=language)) as response:
            response.raise_for_status()
            return Page(**response.json())
    except (requests.RequestException, TypeError) as error:
        message = str(error)
        raise click.ClickException(message)
