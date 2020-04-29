import os
import sys

BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
GIT_DIR = os.path.join(BASE_DIR, ".git")
GITHOOKS_DIR = os.path.join(GIT_DIR, "hooks")
CONFIG_FILE = os.path.join(BASE_DIR, "pyproject.toml")
VALID_HOOKS_NAME = [
    "applypatch-msg",
    "post-update",
    "pre-merge-commit",
    "pre-receive",
    "commit-msg",
    "pre-applypatch",
    "pre-push",
    "prepare-commit-msg",
    "fsmonitor-watchman",
    "pre-commit",
    "pre-rebase",
    "update",
]
