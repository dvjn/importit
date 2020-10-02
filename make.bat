@echo off

SET PY=python -m
SET PY_FILES=importit tests setup.py

IF /I "%1"=="init-pip" GOTO init-pip
IF /I "%1"=="init" GOTO init
IF /I "%1"=="format" GOTO format
IF /I "%1"=="lint" GOTO lint
IF /I "%1"=="test" GOTO test
IF /I "%1"=="test-cov" GOTO test-cov
IF /I "%1"=="make" GOTO make
IF /I "%1"=="init-publish" GOTO init-publish
IF /I "%1"=="publish" GOTO publish
GOTO error

:init-pip
	%PY% pip install -U wheel pip setuptools
	GOTO :EOF

:init
	CALL make.bat init-pip
	%PY% pip install colorama
	%PY% pip install -e .[dev]
	GOTO :EOF

:format
	%PY% isort %PY_FILES%
	%PY% black %PY_FILES%
	GOTO :EOF

:lint
	CALL make.bat format
	%PY% flake8 %PY_FILES%
	GOTO :EOF

:test
	CALL make.bat lint
	%PY% pytest
	GOTO :EOF

:test-cov
	CALL make.bat lint
	%PY% pytest --cov=importit
	GOTO :EOF

:make
	%PY% make_to_batch
	GOTO :EOF

:init-publish
	CALL make.bat init-pip
	%PY% pip install .[publish]
	GOTO :EOF

:publish
	CALL make.bat init-publish
	python setup.py sdist
	python setup.py bdist_wheel
	%PY% twine check dist/*
	%PY% twine upload --non-interactive --skip-existing dist/*
	GOTO :EOF

:error
    IF "%1"=="" (
        ECHO make: *** No targets specified and no makefile found.  Stop.
    ) ELSE (
        ECHO make: *** No rule to make target '%1%'. Stop.
    )
    GOTO :EOF
