# Run:
#   make help
#
# for a description of the available targets


# ------------------------------------------------------------------------- Help target

TARGET_MAX_CHAR_NUM=20
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
RESET  := $(shell tput -Txterm sgr0)

## Show this help message
help:
	@echo ''
	@echo 'Usage:'
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			printf "  ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)s${RESET} ${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)


# ------------------------------------------------------------------------ Clean target

## Delete temp operational stuff like artifacts, test outputs etc
clean:
	rm -rf .mypy_cache/
	rm -rf .pytest_cache/
	rm -f .coverage
	rm -f .coverage.*
	rm -rf htmlcov/


# --------------------------------------------------------- Environment related targets

## Create a virtual environment
env:
	python3 -m venv .venv
	. .venv/bin/activate
	pip install -U pip

## Install pre-commit hooks
pre-commit:
	pip install pre-commit
	pre-commit install

## Install package
init:
	pip install --no-cache-dir -e ".[test]"


# ---------------------------------------------------------------- Test related targets

PYTEST_ARGS = --show-capture no --full-trace --verbose --cov auth/ --cov-report term-missing --cov-report xml

## Run tests
test:
	pytest $(PYTEST_ARGS) $(TESTS_PATH)


# ---------------------------------------------------------- Code style related targets

SRC_CODE = auth/ tests/

## Run the flake linter
flake:
	flake8 $(SRC_CODE)

## Run the black formatter
black:
	black $(SRC_CODE)

## Dry run the black formatter
black-check:
	black --check $(SRC_CODE)

## Run the isort import formatter
isort:
	isort $(SRC_CODE)

## Dry run the isort import formatter
isort-check:
	isort --check $(SRC_CODE)

## Run the mypy static type checker
mypy:
	mypy $(SRC_CODE)

## Format source code
format: black isort

## Check code style
style: flake black-check isort-check # mypy