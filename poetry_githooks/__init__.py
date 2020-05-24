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
        helpers.error("This is not a Git repository. Run 'git init' first")
        sys.exit(1)

    if not os.path.isdir(settings.GITHOOKS_DIR):
        try:
            os.mkdir(settings.GITHOOKS_DIR)
        except OSError:
            helpers.error("Failed to create %s" % settings.GITHOOKS_DIR)
            sys.exit(1)

    hooks.write_all()


@cli.command(context_settings=dict(ignore_unknown_options=True))
@click.option(
    "--name",
    type=click.Choice(settings.VALID_HOOKS_NAME),
    help="Name of the hook to run",
)
@click.argument("args", nargs=-1, type=click.UNPROCESSED)
def run(name, args):
    script = hooks.get_script(name)
    helpers.info(f"Running {name} hook")
    return_code = helpers.execute_script(script, args)
    helpers.info(f"Done running {name} hook")
    sys.exit(return_code)


@cli.command()
@click.option("--force", "-f", is_flag=True)
def reset(force):
    return hooks.reset(force)


if __name__ == "__main__":
    cli()
