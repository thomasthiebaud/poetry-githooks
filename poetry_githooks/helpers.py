import subprocess
import sys
import stat
import os
import toml

from poetry_githooks import settings


def read_config():
    if not os.path.isfile(settings.CONFIG_FILE):
        click.echo("Missing 'pyproject.toml'. Run 'poetry init' to setup a project")
        sys.exit(1)

    try:
        config = toml.load(settings.CONFIG_FILE)
    except toml.TomlDecodeError:
        click.echo("pyproject.toml file is malformed and could not be read")
        sys.exit(1)

    return config


def make_executable(path):
    st = os.stat(path)
    os.chmod(path, st.st_mode | stat.S_IEXEC)


def execute_script(script: str):
    return_code = subprocess.call(f"{script}", shell=True)
    sys.exit(return_code)
