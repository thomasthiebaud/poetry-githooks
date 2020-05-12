import sys
from unittest.mock import patch
import toml
import pytest

from mamba import context, describe, it
from poetry_githooks import helpers

with describe("Helpers"):
    with context("#execute_script"):
        with it("should execute a script without arguments"):
            with patch("subprocess.call") as call_mock, patch("sys.exit") as exit_mock:
                helpers.execute_script("ls")
                call_mock.assert_called_with("ls", shell=True)
        with it("should execute a script with static arguments"):
            with patch("subprocess.call") as call_mock, patch("sys.exit") as exit_mock:
                helpers.execute_script("ls -l")
                call_mock.assert_called_with("ls -l", shell=True)
        with it(
            "should execute a script with dynamic arguments and escape them if necessary"
        ):
            with patch("subprocess.call") as call_mock, patch("sys.exit") as exit_mock:
                helpers.execute_script("ls", ["-l", "somefile; rm -rf ~"])
                call_mock.assert_called_with("ls -l 'somefile; rm -rf ~'", shell=True)
    with context("#read_config"):
        with it("should exit if the config is not present"):
            with patch("os.path.isfile", return_value=False) as isfile_mock, patch(
                "sys.exit"
            ) as exit_mock, patch("toml.load") as toml_mock:
                helpers.read_config()
                args, kwargs = exit_mock.call_args
                assert args[0] == 1
        with it("should exit if config is present but malformed"):
            with patch("os.path.isfile", return_value=True) as isfile_mock, patch(
                "sys.exit"
            ) as exit_mock, patch(
                "toml.load", side_effect=toml.TomlDecodeError("Error", "", 0)
            ) as toml_mock:
                helpers.read_config()
                args, kwargs = exit_mock.call_args
                assert args[0] == 1
