Usage
=====

.. _installation:

Installation
------------

To use RTD Test, first install it using pip:

.. code-block:: console

   (.venv) $ pip install rtd_test_project

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``rtd_test_project.get_random_ingredients()`` function:

.. autofunction:: rtd_test_project.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`rtd_test_project.get_random_ingredients`
will raise an exception.

.. autoexception:: rtd_test_project.InvalidKindError

For example:

.. runblock:: pycon

    >>> import rtd_test_project
    >>> rtd_test_project.get_random_ingredients()
    ['shells', 'gorgonzola', 'parsley']

