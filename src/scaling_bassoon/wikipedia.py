import click
import pydantic
import requests

API_URL = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"


class Page(pydantic.BaseModel):
    title: str
    extract: str


def random_page(language: str = "en") -> Page:
    try:
        with requests.get(API_URL.format(language=language)) as response:
            response.raise_for_status()
            return Page(**response.json())
    except (requests.RequestException, TypeError) as error:
        message = str(error)
        raise click.ClickException(message)
