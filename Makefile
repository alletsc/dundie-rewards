.PHONY: install virtualenv ipython clean test watch testci
install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	@echo "Creating virtual environment"
	@.venv/bin/python -m pip -m venv .venv

ipython:
	@echo "Starting IPython"
	@.venv/bin/ipython

test:
	@.venv/bin/pytest -s

testci:
	@.venv/bin/pytest -v --junitxml=test-result.xml

watch:
	#@.venv/bin/ptw -- -vv -s tests/
	@ls **/*.py | entr pytest

clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build
