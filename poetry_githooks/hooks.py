import toml
import click
import os
import sys

from poetry_githooks import settings, helpers


def _get_raw_hooks():
    config = helpers.read_config()

    try:
        hooks = config["tool"]["githooks"]
    except KeyError:
        helpers.error(
            "No hooks found. Add a [tool.githooks] section to your pyproject.toml"
        )
        sys.exit(1)

    return hooks


def get_script(hook: str):
    hooks = _get_raw_hooks()

    try:
        script = hooks[hook]
    except KeyError:
        helpers.error(
            f"No hooks called {hook} found. Add a [tool.githooks] section to your pyproject.toml with the desired hook"
        )
        sys.exit(1)

    return script


def read():
    hooks = _get_raw_hooks()

    for hook, script in hooks.items():
        if hook not in settings.VALID_HOOKS_NAME:
            helpers.error(f"'{hook}' is not a valid hook")
            sys.exit(1)

        yield (hook, script)


def reset(force=False):
    for hook in settings.VALID_HOOKS_NAME:
        hook_path = os.path.join(settings.GITHOOKS_DIR, hook)

        try:
            with open(hook_path, "r+") as hook_file:
                if force or settings.SIGNATURE in hook_file.read():
                    hook_file.close()
                    os.remove(hook_path)

        except FileNotFoundError:
            pass


def write(hook: str):
    hook_path = os.path.join(settings.GITHOOKS_DIR, hook)

    if os.path.isfile(hook_path):
        helpers.info(f"Skiping {hook} setup because {hook_path} already exists")
    else:
        with open(hook_path, "w+") as hook_file:
            hook_file.write(
                f"""#!/bin/bash
{settings.SIGNATURE}
poetry run githooks run --name {hook} $@"""
            )

        helpers.make_executable(hook_path)


def write_all():
    reset()

    for (hook, script) in read():
        write(hook)
