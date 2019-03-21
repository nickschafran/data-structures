Data Structures
===============

This repository contains implementation of a few basic data structures in
Python 2.7. It exists for non-commercial, self-learning purposes. Tests are run 
using ``nose`` (See the Environment Setup section).

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

Environment Setup
-----------------

To setup local environment and run unit tests::

   $ pipenv install --dev
   $ pipenv run nosetests --with-coverage --cover-html

