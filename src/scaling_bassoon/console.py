import textwrap

import click

from . import __version__, wikipedia


@click.command()
@click.version_option(version=__version__)
@click.option("--lang", default="en", help="Language of an article")
def main(lang):
    """The hypermodern Python project."""
    data = wikipedia.random_page(lang)

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
