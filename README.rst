|Build Status| |Coverage Status| |PyPI Version| |Wheel Status|

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


.. |Build Status| image:: https://img.shields.io/travis/tonyseek/python-base36.svg?style=flat
   :target: https://travis-ci.org/tonyseek/python-base36
   :alt: Build Status
.. |Coverage Status| image:: https://img.shields.io/coveralls/tonyseek/python-base36.svg?style=flat
   :target: https://coveralls.io/r/tonyseek/python-base36
   :alt: Coverage Status
.. |Wheel Status| image:: https://pypip.in/wheel/base36/badge.svg?style=flat
   :target: https://warehouse.python.org/project/base36
   :alt: Wheel Status
.. |PyPI Version| image:: https://img.shields.io/pypi/v/base36.svg?style=flat
   :target: https://pypi.python.org/pypi/base36
   :alt: PyPI Version
