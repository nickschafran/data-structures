.. Data Structures documentation master file, created by
   sphinx-quickstart on Sun Dec  4 04:22:48 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Data Structures
===============

This repository contains implementation of a few basic data structures in
Python (2 and 3 compatible, unless noted). It exists for non-commercial,
self-learning purposes. Tests are run using ``nose``, using the
included ``run_coverage_tests.sh`` 'script'.

Some of the implementations draw from the book "Problem Solving with Algorithms
and Data Structures using Python" by Bradley N. Miller, David L. Ranum (©
Copyright 2014 Brad Miller, David Ranum; licensed under the `Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International License
<https://creativecommons.org/licenses/by-nc-sa/4.0/>`_), and are noted as such
in the files containing derivative works. In according with the terms of the
license, this work is also distributed under the same license (see ``LICENSE``).
I reccomend the book highly for those learning data structures. It can be read
in online form
`here <https://interactivepython.org/runestone/static/pythonds/index.html>`_.

User Guide
----------

Using this package is as easy as downloading and installing:

.. code-block:: shell

    git clone https://github.com/nickschafran/data-structures.git
    cd data-structures
    python setup.py install


Then, open up a python interpreter and get started!

.. code-block:: python

    >>> import data_structures
    >>> bst = BinarySearchTree()
    >>> bst[4] = 1
    >>> bst[2] = 3
    >>> bst[3] = 5
    >>> 3 in bst
    True

Module Documentation:
---------------------

.. toctree::
   :maxdepth: 2

   modules/stack
   modules/deque
   modules/queue
   modules/binary_search_tree
   modules/linked_list