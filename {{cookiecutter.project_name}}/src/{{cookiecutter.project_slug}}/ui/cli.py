import logging
from pprint import pprint

import typer

from {{cookiecutter.project_slug}}.app import App
from {{cookiecutter.project_slug}}.config import get_default_settings

cli = typer.Typer()
app = App()
log = logging.getLogger(__name__)


@cli.command()
def hello(name: str):
    log.info("hello, world")
    print(f"hello, {name}")


@cli.command(name="info", help="Print App Info")
def info():
    pprint(get_default_settings().to_dict())
