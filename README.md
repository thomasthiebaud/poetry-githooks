# poetry-githooks

## Install

This repository is made to work with [poetry](https://python-poetry.org/). Assuming you have a working `poetry` setup, run

```
poetry add -D poetry-githooks
```

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
