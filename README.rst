**Author**: `Pahaz Blinov`_

**Repo**: https://github.com/pahaz/py3line/

Pyline is a UNIX command-line tool for line-based processing
in Python with regex and output transform features
similar to grep, sed, and awk.

This project inspired by: `piep`_, `pysed`_, `pyline`_, `pyp`_ and
`Jacob+Mark recipe <https://code.activestate.com/recipes/437932-pyline-a-grep-like-sed-like-command-line-tool/>`_

**requirements**: Python3

**WHY I MAKE IT?**

I sometimes have to use `sed` / `awk`.
Not often, and so I always forget the necessary options and `sed` / `awk` DSL.
But I now python, I like it, and I want use it for data processing.
Default `python -c` is hard to write the kind of one-liner that works well.

Why not a `pyline`?
 * Don`t support python3
 * Have many options (I want as much simple as possible solution)
 * Bad performance
 * Don`t support command chaining

Why not a `pysed`?
 *

Installation
============

`py3line`_ is on PyPI, so simply run:

::

    pip install py3line

or ::

    easy_install py3line

to have it installed in your environment.

For installing from source, clone the
`repo <https://github.com/pahaz/py3line>`_ and run::

    python setup.py install

Usage scenarios
===============

...

Examples
--------

Example 1: create spreadsheet
=============================

.. code-block:: bash

    $ echo -e "Here are\nsome\nwords for you." | ./py3line.py "x.split()" -a "len(x)"
    2
    1
    3

DOCS
----

.. _Pahaz Blinov: https://github.com/pahaz/
.. _py3line: https://pypi.python.org/pypi/py3line/
.. _pyp: https://pypi.python.org/pypi/pyp/
.. _piep: https://github.com/timbertson/piep/tree/master/piep/
.. _pysed: https://github.com/dslackw/pysed/blob/master/pysed/main.py
.. _pyline: https://github.com/westurner/pyline/blob/master/pyline/pyline.py
