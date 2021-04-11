import click
import requests


def random_page(language="en"):
    api_url = f"https://{language.lower()}.wikipedia.org/api/rest_v1/page/random/summary"
    try:
        with requests.get(api_url) as response:
            response.raise_for_status()
            return response.json()
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message)

