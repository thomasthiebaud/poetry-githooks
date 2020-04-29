import toml
import click
import os

from poetry_githooks import settings, helpers


def _get_raw_hooks():
    config = helpers.read_config()

    try:
        hooks = config["tool"]["githooks"]
    except KeyError:
        click.echo(
            "No hooks found. Add a [tool.githooks] section to your pyproject.toml"
        )
        sys.exit(1)

    return hooks


def get_script(hook: str):
    hooks = _get_raw_hooks()

    try:
        script = hooks[hook]
    except KeyError:
        click.echo(
            f"No hooks called {hook} found. Add a [tool.githooks] section to your pyproject.toml with the desired hook"
        )
        sys.exit(1)

    return script


def read():
    hooks = _get_raw_hooks()

    for hook, script in hooks.items():
        if hook not in settings.VALID_HOOKS_NAME:
            click.echo(f"'{hook}' is not a valid hook")
            sys.exit(1)

        yield (hook, script)


def write(hook: str):
    hook_path = os.path.join(settings.GITHOOKS_DIR, hook)

    with open(hook_path, "w+") as hook_file:
        hook_file.write(
            f"""#!/bin/bash

poetry run githooks {hook} $@
        """
        )

    helpers.make_executable(hook_path)


def write_all():
    for (hook, script) in read():
        write(hook)
