Base36 in Python
================

Yet another implementation for the positional numeral system using 36 as the radix.


Installation
------------

.. code-block:: shell

    pip install base36


Usage
-----

.. code-block:: python

    import base36

    assert base36.dumps(19930503) == 'bv6h3'
    assert base36.loads('bv6h3') == 19930503


Issues
------

If you want to report bugs or request features, please create issues on
`GitHub Issues <https://github.com/tonyseek/python-base36/issues>`_.


Contributes
-----------

You can send a pull reueqst on
`GitHub <https://github.com/tonyseek/python-base36/pulls>`_.
