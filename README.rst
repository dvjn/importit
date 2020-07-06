========
importit
========

|Package Version Badge| |Package Downloads Badge|

Import python code from anywhere.


Installation
------------

.. code-block:: shell

    pip install importit


Examples
--------


Importing gist
~~~~~~~~~~~~~~

We will import this gist: `Test Gist <https://gist.github.com/divykj/51dcf067f4e445c3f837d26efd2c138e>`_ (id: 51dcf067f4e445c3f837d26efd2c138e)

.. code-block:: python3

    from importit import import_gist

    # Importing whole gist
    # We give it the module name and gist id from the end of the gist link.
    hellos = import_gist("hellos", "51dcf067f4e445c3f837d26efd2c138e")
    hellos.hello.say_hello() # output: hello
    hellos.hello_again.say_hello_again() # output: hello again

    # Importing specific file from the gist
    import_gist("hellos", "51dcf067f4e445c3f837d26efd2c138e")

    from hellos import hello
    hello.say_hello() # output: hello



Importing python file
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python3

    from importit import import_local_file, import_remote_file

    foo = import_local_file("foo", local_python_file_path)
    bar = import_remote_file("bar", remote_python_file_url)


Importing python code
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python3

    from importit import import_code

    python_code = """
    def say_hello():
        print("hello")
    """
    dummy = import_code("dummy", python_code)
    dummy.say_hello() # output: hello


.. |Package Downloads Badge| image:: https://img.shields.io/pypi/dm/importit
    :alt: Package Downloads

.. |Package Version Badge| image:: https://img.shields.io/pypi/v/importit?label=version
    :alt: Package Version
