import textwrap

import click
import requests

from . import __version__




@click.command()
@click.version_option(version=__version__)
@click.option("--lang", default="en", help="Language of an article")
def main(lang):
    """The hypermodern Python project."""

    api_url = f"https://{lang.lower()}.wikipedia.org/api/rest_v1/page/random/summary"
    with requests.get(api_url) as response:
        response.raise_for_status()
        data = response.json()

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
