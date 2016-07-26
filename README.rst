|CircleCI| |coveralls| |version|

|DwnMonth| |DwnWeek| |DwnDay|

|pyversions| |license|

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

If you don`t have **pip** you can `install it <https://pip.pypa.io/en/stable/installing/#installation>`_

Typical use case
================

You write a text processed util or script and you want to test it.

For example, we want test **ls** util.

All of we need is create **test_ls.bashtest** file::

    $ ls ./testsuit/list-directory
    file1
    file2.txt
    file3.py
    file4.sh

and then run tests ::

    $ bashtest test_ls.bashtest
    1 items passed all tests:
       1 tests in test_ls.bashtest
    1 tests in 1 items.
    1 passed and 0 failed.
    Test passed.

Test README examples
====================

You have a some open source project like this. And of course, as in any good
open source project, you have examples. You can automatically check this
examples. Just add **bashtest README.rst** in your CI tests.

More examples
=============

You can finde some examples in this project. Please check **test_*.bashtest**
files

HELP
----

::

    usage: bashtest [-h] [--exitcode] [--no-blankline-substitution]
                    [--no-normalize-whitespace] [-v] [-q] [--version]
                    file [file ...]

    BashTest is a UNIX command-line tool for running text-based bash tests.

    positional arguments:
      file                  Input file

    optional arguments:
      -h, --help            show this help message and exit
      --exitcode            Print exitcode after command end of output
      --no-blankline-substitution
                            Substitute `<BLANKLINE>` if an expected output block
                            contains a line containing only the `\n`
      --no-normalize-whitespace
                            All sequences of whitespace (blanks and newlines) are
                            not equal
      -v, --verbose
      -q, --quiet
      --version             Print the version string


.. _Pahaz Blinov: https://github.com/pahaz/
.. _bashtest: https://pypi.python.org/pypi/bashtest
.. |CircleCI| image:: https://circleci.com/gh/pahaz/bashtest.svg?style=svg
   :target: https://circleci.com/gh/pahaz/bashtest
.. |coveralls| image:: https://coveralls.io/repos/github/pahaz/bashtest/badge.svg?branch=master
   :target: https://coveralls.io/github/pahaz/bashtest?branch=master
.. |DwnMonth| image:: https://img.shields.io/pypi/dm/bashtest.svg
.. |DwnWeek| image:: https://img.shields.io/pypi/dw/bashtest.svg
.. |DwnDay| image:: https://img.shields.io/pypi/dd/bashtest.svg
.. |pyversions| image:: https://img.shields.io/pypi/pyversions/bashtest.svg
.. |version| image:: https://img.shields.io/pypi/v/bashtest.svg
   :target: `bashtest`_
.. |license| image::  https://img.shields.io/pypi/l/bashtest.svg
   :target: https://github.com/pahaz/bashtest/blob/master/LICENSE
