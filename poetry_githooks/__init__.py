import os
import sys
import toml
import click

from poetry_githooks import helpers, hooks


@click.group()
def cli():
    pass


@cli.command()
def setup():
    if not os.path.isdir(settings.GIT_DIR):
        click.echo("This is not a Git repository. Run 'git init' first")
        sys.exit(1)

    if not os.path.isdir(settings.GITHOOKS_DIR):
        try:
            os.mkdir(settings.GITHOOKS_DIR)
        except OSError:
            click.echo("Failed to create %s" % settings.GITHOOKS_DIR)
            sys.exit(1)

    hooks.write_all()


@cli.command()
def pre_commit():
    script = hooks.get_script("pre-commit")
    return helpers.execute_script(script)


if __name__ == "__main__":
    cli()
