SIMILARITY SEARCHING IN METRICS SPACES USING SKETCHES
=====================================================

This package contains implementation of experiments and documentation for my Diploma Thesis.

Description
-------------------

    Please note this is just informal description. For correct and exact definitions of Metric space Similarity searching
    see 'Similarity Search, The Metric Space Approach' by Zezula, P., Amato, G., Dohnal, V., Batko, M.
    http://www.springer.com/gp/book/9780387291468

What's typical problem solved by Similarity Searching?

    We have large database of objects (e.g. float vectors, images, text documents) and we receive some query object
    that's comparable with objects in our database using some distance function (e.g. Hamming distance, Jaccard distance).
    Our task is for this query object retrieve all objects from the database within some distance range or to retrieve
    k nearest objects. On large databases this is usually done by organizing database objects into some
    index (e.g. B-Tree, M-Tree) which reduces number of distance computations needed for receiving similar objects.
    To reduce number of distance computations we can use partitioning methods (e.g. Ball partitioning, Hyperplane partitioning)
    which split search space in multiple areas and some clever filtering techniques to filter out some areas of space,
    leaving us with less candidates to examine for being similar to query object.

What are Sketches?

    Sketches are binary codes of fixed length that are used to represent database objects for fast Similarity searching.
    They are stored in RAM and compared by Hamming distance which can be implemented using hardware operations. Sketches
    can be also organized into index to reduce number of distance computations. When query object is received, first it's
    Sketch is constructed and Sketchces similar to his are identified. After that only database items with similar
    Sketches are needed to be examined as candidates for result.

Thesis
------

Goal

    The goal of this thesis is to research, implement and evaluate Multi-index Hashing for Similarity searching on
    Sketches.

    http://www.cs.toronto.edu/~norouzi/research/papers/multi_index_hashing.pdf

Thesis will be written and stored in separate Git repository using Thesis skeleton from:

.. code-block:: shell

    https://github.com/Witiko/fithesis3.git


DEVELOPMENT
===========

Install requirements manually if needed:

.. code-block:: shell

    pip install -r requirements.txt

Install package for developement:

.. code-block:: shell

    python setup.py develop

Install package for production:

.. code-block:: shell

    python setup.py install

Run tests:

.. code-block:: shell

    py.test

Commit:

.. code-block:: shell

    git pull
    git commit -am 'commit message'
    git push

IPYTHON NOTEBOOKS
=================

http://jupyter.org

Run notebooks in browser:

.. code-block:: shell

    jupyter notebook

REFERENCES
==========

bitstring documentation:

    http://pythonhosted.org/bitstring/index.html