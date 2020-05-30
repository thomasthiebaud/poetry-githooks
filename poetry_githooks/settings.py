import os
import sys

BASE_DIR = os.path.realpath(".")
GIT_DIR = os.path.join(BASE_DIR, ".git")
GITHOOKS_DIR = os.path.join(GIT_DIR, "hooks")
CONFIG_FILE = os.path.join(BASE_DIR, "pyproject.toml")

SIGNATURE = "# created with poetry-githooks"

# List from https://git-scm.com/docs/githooks#_hooks
VALID_HOOKS_NAME = [
    "applypatch-msg",  # 1 parameter
    "pre-applypatch",  # No parameter
    "post-applypatch",  # No parameter
    "pre-commit",  # No parameter
    "pre-merge-commit",  # No parameter
    "prepare-commit-msg",  # 1-3 parameter
    "commit-msg",  # 1 parameter
    "post-commit",  # No parameter
    "pre-rebase",  # 1-2 parameters
    "post-checkout",  # 3 parameters
    "post-merge",  # 1 parameter
    "pre-push",  # 2 parameters
    "pre-receive",  # No parameter
    "update",  # 3 parameters
    "post-receive",  # No parameter
    "post-update",  # variable number of parameters
    "push-to-checkout",  # 1 parameter
    "pre-auto-gc",  # No parameter
    "post-rewrite",  # 1 parameter
    "sendemail-validate",  # 1 parameter
    "fsmonitor-watchman",  # 1-2 parameter
    "p4-pre-submit",  # No parameter
    "post-index-change",  # 2 parameters
]
