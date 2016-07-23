**Author**: `Pahaz Blinov`_

**Repo**: https://github.com/pahaz/bashtest/

BashTest is a UNIX command-line tool for bash/shell utils unit testing.

This is a simplest way to write a simple bash tests.

**requirements**: Python2 or Python3

Installation
============

`bashtest`_ is on PyPI, so simply run:

::

    pip install bashtest

or ::

    easy_install bashtest

to have it installed in your environment.

For installing from source, clone the
`repo <https://github.com/pahaz/bashtest>`_ and run::

    python setup.py install

If you don`t have `pip` you can `install it <https://pip.pypa.io/en/stable/installing/#installation>`_

Typical use case
================

You write a text processed util or script and you want to test it.

For example, we want test `ls` util.

All of we need is create `test_ls.bashtest` file::

    $ ls ./testsuit/list-directory
    file1
    file2.txt
    file3.py
    file4.sh

and then run tests ::

    $ python -m bashtest test_ls.bashtest
    1 items passed all tests:
       1 tests in test_ls.bashtest
    1 tests in 1 items.
    1 passed and 0 failed.
    Test passed.

Test README examples
====================

You have a some open source project like this. And of course, as in any good
open source project, you have examples. You can automatically check this
examples. Just add `python -m bashtest README.rst` in your CI tests.

More examples
=============

You can finde some examples in this project. Please check `test_*.bashtest`
files

DOCS
----

.. _Pahaz Blinov: https://github.com/pahaz/
