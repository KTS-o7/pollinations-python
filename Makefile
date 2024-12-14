# Description: Makefile for the project pypollination
PYTHON := python3
PIP := pip3
POETRY := poetry

# Targets
.PHONY: all install test  format clean

all: install test format

install:
    $(POETRY) install

test:
    $(POETRY) run pytest

format:
    $(POETRY) run black .

clean:
    $(POETRY) env remove -n $(shell $(POETRY) env info --path)
    rm -rf __pycache__
    rm -rf .pytest_cache
    rm -rf .mypy_cache
    rm -rf .coverage
    rm -rf htmlcov