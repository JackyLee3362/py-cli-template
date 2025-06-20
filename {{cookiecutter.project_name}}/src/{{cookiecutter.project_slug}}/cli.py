import logging

import typer

import {{cookiecutter.project_slug}}

log = logging.getLogger(__name__)
cli = typer.Typer()


@cli.command()
def hello(name: str):
    log.info("hello, world")
    print(f"hello, {name}")


@cli.command(name="info")
def info():
    print({{cookiecutter.project_slug}}.PACKAGE_PATH)
    print({{cookiecutter.project_slug}}.SRC_PATH)
