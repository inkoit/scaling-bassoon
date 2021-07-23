"""Command-line interface."""

import textwrap

import click

from . import __version__, wikipedia


@click.command()
@click.version_option(version=__version__)
@click.option(
    "--language",
    "-l",
    default="en",
    help="Language edition of Wikipedia",
    metavar="LANG",
    show_default=True,
)
def main(language: str) -> None:
    """The hypermodern Python project."""
    data = wikipedia.random_page(language=language)

    click.secho(data.title, fg="green")
    click.echo(textwrap.fill(data.extract))
