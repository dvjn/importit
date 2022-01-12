# Contributing

## Issues

Issues are very valuable to this project.

- Ideas are a valuable source of contributions others can make
- Problems show where this project is lacking
- With a question you show where contributors can improve the user experience

Thank you for creating them.

## Developing

[Create and activate a Python 3 virtual environment.](https://docs.python.org/3/tutorial/venv.html)

All the commands required for development are managed by `Makefile`

- For linux and macOS, use `make [command]`
- For windows, use `.\make.bat [command]`

| Command    | Description                                                           |
| ---------- | --------------------------------------------------------------------- |
| `init`     | Installs the dev dependencies                                         |
| `format`   | Formats all the python files (with isort and black)                   |
| `lint`     | Lints the code (with flake8)                                          |
| `test`     | Runs all tests (with pytest)                                          |
| `test-cov` | Runs all tests with coverage metrics (with pytest and pytest-cov)     |
| `make`     | Generates make.bat from Makefile (always use after updating Makefile) |

## Pull Requests

Pull requests are, a great way to get your ideas into this repository.

When deciding if I merge in a pull request I look at the following things:

### Does it state intent

You should be clear which problem you're trying to solve with your contribution.

Tell me the problem that you have found, and the in pull request show me the action you have taken to solve it.

### Is it of good quality

- It passes all the tests
- There are no additional warnings introduced
- Proper tests are added to test the new code
- It follows the code style of the project
- There are no spelling mistakes
- It is pythonic and reads well

### Does it move this repository closer to my vision for the repository

The aim of this repository is:

- To provide an easier way to dynamically import python code from different sources.
- Make this project as beginner friendly as possible.
- Foster a culture of respect and gratitude in the open source community.

### Does it follow the contributor covenant

This repository has a [code of conduct](CODE_OF_CONDUCT.md), This repository has a code of conduct, I will remove things that do not respect it.
