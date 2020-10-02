PY = python -m
PY_FILES = importit tests setup.py

init-pip:
	$(PY) pip install -U wheel pip setuptools

init: init-pip
	$(PY) pip install colorama # TODO: remove when make-to-batch fixes issue#1
	$(PY) pip install -e .[dev]

format:
	$(PY) isort $(PY_FILES)
	$(PY) black $(PY_FILES)

lint: format
	$(PY) flake8 $(PY_FILES)

test: lint
	$(PY) pytest

test-cov: lint
	$(PY) pytest --cov=importit

make:
	$(PY) make_to_batch

init-publish: init-pip
	$(PY) pip install .[publish]

publish: init-publish
	python setup.py sdist
	python setup.py bdist_wheel
	$(PY) twine check dist/*
	$(PY) twine upload --non-interactive --skip-existing dist/*
