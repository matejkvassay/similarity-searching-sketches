SIMILARITY SEARCHING IN METRICS SPACES USING SKETCHES
=====================================================

This package contains implementation of experiments and documentation for my Diploma Thesis.

Problem description
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
    which split search space in multiple areas and some clever filtering techniques to filter out some areas of space
    leaving us with fewer candidates to less candidates examine for being similar to our query.

What are Sketches?

    Sketches are binary codes of fixed length that are used to represent database objects for fast Similarity searching.
    They are stored in RAM and compared by Hamming distance which can be implemented using hardware operations. Sketches
    can be also organized into index to reduce number of distance computations. When query object is received, first it's
    Sketch is constructed and Sketchces similar to his are identified. After that only database items with similar
    Sketches are needed to be examined as candidates for result.

Thesis
------

Goal

    The goal of this thesis is to research, implement and evaluate similarity searching on metric Sketches using
    Multi-Index Hashing.

Thesis will be written and stored in separate Git repository using Thesis skeleton from:

.. code-block:: shell

    git clone https://github.com/Witiko/fithesis3.git