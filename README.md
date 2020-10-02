<div align="center">

![banner](https://raw.githubusercontent.com/divykj/importit/master/banner.svg "importit banner")

# importit

![importit downloads badge](https://img.shields.io/pypi/dm/importit?color=84dbff&style=flat-square "importit downloads")
![importit version badge](https://img.shields.io/pypi/v/importit?label=version&color=ffd05b&style=flat-square "importit version")
![importit python versions badge](https://img.shields.io/pypi/pyversions/importit?color=e6e9ee&style=flat-square "importit python versions")

</div>

> Import python code from anywhere.

**`importit`** is a python code import helper. Using it, you can dynamically import python code from different sources (like gists, python files on the internet, local python files). You don't need to copy python code snippets from project to project.

Some of use cases can be:

- Reusing python code snippets in multiple places and projects
- Dynamically reloading python code on live environments
- You tell me, what will you use it for?

---

### From where do you want to import?

<details>
<summary><b>Github Gist</b></summary>

<br />

Find the gist id from the gist url: `https://gist.github.com/<username>/<gist id>`

Using [this gist](https://gist.github.com/divykj/51dcf067f4e445c3f837d26efd2c138e) as an exmaple:

```python
from importit import import_gist

imported_gist = import_gist("imported_gist", "51dcf067f4e445c3f837d26efd2c138e")

imported_gist.first_file.some_function()
imported_gist.second_file.some_other_function()
```

**Note:** The gist will be imported in the form of module, with each python file in the gist as a submodule.

</details>

<details>
<summary><b>Remote File</b></summary>

<br />

Use any valid python file url (for example, [`http://bit.ly/aPythonFile`](http://bit.ly/aPythonFile))

```python
from importit import import_remote_file

imported_file = import_remote_file("imported_file", "http://bit.ly/aPythonFile")

imported_file.some_function()
```

</details>

<details>
<summary><b>Local File</b></summary>

```python
from importit import import_remote_file

imported_file = import_remote_file("imported_file", "/home/divykj/aPythonFile.py")

imported_file.some_function()
```

</details>

<details>
<summary><b>Code Snippet</b></summary>

```python
from importit import import_code

python_code = """
def some_function():
    # do some crazy things
    pass
"""

imported_code = import_code("imported_code", python_code)
imported_code.some_function()
```

</details>

Planning to add **Github**, **Gitlab**, **Bitbucket** (and other git repository services) and maybe **PyPI** support soon.

---

### How to install?

```shell
❯ pip install importit
```
