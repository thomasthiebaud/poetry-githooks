import sys
from unittest.mock import patch
import toml

from poetry_githooks import helpers

from unittest import TestCase


class TestHelpers(TestCase):
    def test_execute_script_without_argument(self):
        with patch("subprocess.call") as call_mock, patch("sys.exit") as exit_mock:
            helpers.execute_script("ls")
            call_mock.assert_called_with("ls", shell=True)

    def test_execute_script_with_static_argument(self):
        with patch("subprocess.call") as call_mock, patch("sys.exit") as exit_mock:
            helpers.execute_script("ls -l")
            call_mock.assert_called_with("ls -l", shell=True)

    def test_execute_script_with_dynamic_arguments_and_escape_if_necessary(self):
        with patch("subprocess.call") as call_mock, patch("sys.exit") as exit_mock:
            helpers.execute_script("ls", ["-l", "somefile; rm -rf ~"])
            call_mock.assert_called_with("ls -l 'somefile; rm -rf ~'", shell=True)

    def test_exit_if_config_not_present(self):
        with patch("os.path.isfile", return_value=False) as isfile_mock, patch(
            "sys.exit"
        ) as exit_mock, patch("toml.load") as toml_mock:
            helpers.read_config()
            args, kwargs = exit_mock.call_args
            assert args[0] == 1

    def test_exit_if_config_malformed(self):
        with patch("os.path.isfile", return_value=True) as isfile_mock, patch(
            "sys.exit"
        ) as exit_mock, patch(
            "toml.load", side_effect=toml.TomlDecodeError("Error", "", 0)
        ) as toml_mock:
            helpers.read_config()
            args, kwargs = exit_mock.call_args
            assert args[0] == 1
