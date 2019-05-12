|CircleCI| |version|

|pyversions| |license|

**Author**: `Pahaz Blinov`_

**Repo**: https://github.com/pahaz/bashtest/

BashTest is a UNIX command-line tool for the testing bash/shell utilites.

This is a simplest way to write simple bash tests.

**requirements**: Python2 or Python3

**keywords**: bash unittest, unittesting, bash tesing, sh unit testing

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

You have a command line util or bash/sh script and you want to test it.

For example, we want to test **ls** util.

All of we need is to create text file with execution log.

**./test_ls.bashtest** ::

    $ ls ./testsuit/list-directory
    file1
    file2.txt
    file3.py
    file4.sh

Run this tests ::

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

changelog
=========

** 0.0.8 **
 - add ``#skipbashtest`` support

** 0.0.7 **
 - fix! remove ugly and useless options
 - feat! Test README.rst `#4 <https://github.com/pahaz/bashtest/issues/4>`_
 - feat! find \*.bashtest by default `#3 <https://github.com/pahaz/bashtest/issues/3>`_

** 0.0.6 **
 - fix! bad command escaping bug `#5 <https://github.com/pahaz/bashtest/issues/5>`_

HELP
----

::

   $ bashtest --help
   usage: bashtest [-h] [--exitcode] [-v] [-q] [--debug] [--version]
                   [file [file ...]]

   BashTest is a UNIX command-line tool for running text-based bash tests.

   positional arguments:
     file           Input file (by default uses *.bashtest)

   optional arguments:
     -h, --help     show this help message and exit
     --exitcode     Print exitcode after command end of output
     -v, --verbose  Verbose output mode
     -q, --quiet    Silent output mode
     --debug        Print the debug information
     --version      Print the version string


.. _Pahaz Blinov: https://github.com/pahaz/
.. _bashtest: https://pypi.python.org/pypi/bashtest
.. |CircleCI| image:: https://circleci.com/gh/pahaz/bashtest.svg?style=svg
   :target: https://circleci.com/gh/pahaz/bashtest
.. |DwnMonth| image:: https://img.shields.io/pypi/dm/bashtest.svg
.. |DwnWeek| image:: https://img.shields.io/pypi/dw/bashtest.svg
.. |DwnDay| image:: https://img.shields.io/pypi/dd/bashtest.svg
.. |pyversions| image:: https://img.shields.io/pypi/pyversions/bashtest.svg
.. |version| image:: https://img.shields.io/pypi/v/bashtest.svg
   :target: `bashtest`_
.. |license| image::  https://img.shields.io/pypi/l/bashtest.svg
   :target: https://github.com/pahaz/bashtest/blob/master/LICENSE
