import subprocess
import sys
import stat
import os
import toml
import shlex
import click

from poetry_githooks import settings


def info(message):
    click.echo(click.style(message, fg="green"))


def error(message):
    click.echo(click.style(message, fg="red"))


def read_config():
    if not os.path.isfile(settings.CONFIG_FILE):
        error("Missing 'pyproject.toml'. Run 'poetry init' to setup a project")
        sys.exit(1)

    try:
        config = toml.load(settings.CONFIG_FILE)
        return config
    except toml.TomlDecodeError:
        error("pyproject.toml file is malformed and could not be read")
        sys.exit(1)


def make_executable(path):
    st = os.stat(path)
    os.chmod(path, st.st_mode | stat.S_IEXEC)


def execute_script(script: str, args=None):
    if args is not None:
        command = " ".join([script] + [shlex.quote(arg) for arg in args])
    else:
        command = script

    return_code = subprocess.call(command, shell=True)
    return return_code
