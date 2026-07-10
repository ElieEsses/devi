.PHONY: install run lint format test fix ci

install:
	uv sync
	uv tool install -e .

run:
	uv run edev --help

lint:
	uv run ruff check .

format:
	uv run ruff format .

fix:
	uv run ruff check . --fix
	uv run ruff format .

test:
	uv run pytest

ci:
	uv run ruff check . --fix
	uv run ruff format --check .
	uv run pytest