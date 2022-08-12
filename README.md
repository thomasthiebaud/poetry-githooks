# poetry-githooks

## Install

This repository is made to work with [poetry](https://python-poetry.org/). Assuming you have a working `poetry` setup, run

```
poetry add -D poetry-githooks
```
If your root git directory is not the project directory, define `POETRY_GITHOOKS_GIT_ROOT` environment variable
and set it to the directory that `.git` resides in.<br>
(For example, if the path to `.git` is `/somepath/.git`, then you should set `POETRY_GITHOOKS_GIT_ROOT=/somepath/`)
## Install

Create a `tool.githooks` section in your `pyproject.toml` file and define your git hooks, for example

```
[tool.githooks]
pre-commit = "black ."
```

then run

```
poetry run githooks setup
```

That's it :tada: your hooks will be ran using `poetry` when expected

**IMPORTANT** You need to rerun `poetry run githooks setup` everytime you change `[tool.githooks]`
