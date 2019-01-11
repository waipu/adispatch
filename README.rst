Multiple Dispatch
=================

|Build Status|

A relatively sane approach to multiple dispatch in Python.

Forked from to support and use annotations for dispatch.
This implementation of multiple dispatch is efficient, mostly complete,
performs static analysis to avoid conflicts, and provides optional namespace
support. It looks good too.


Example
-------

.. code-block:: python

   >>> from adispatch import adispatch

   >>> @adispatch()
   ... def add(x: int, y: int):
   ...     return x + y

   >>> @adispatch()
   ... def add(x: object, y: object):
   ...     return "%s + %s" % (x, y)

   >>> add(1, 2)
   3

   >>> add(1, 'hello')
   '1 + hello'

What this does
--------------

-  Dispatches on all non-keyword arguments

-  Supports inheritance

-  Supports instance methods

-  Supports union types, e.g. ``(int, float)``

-  Supports builtin abstract classes, e.g. ``Iterator, Number, ...``

-  Caches for fast repeated lookup

-  Identifies possible ambiguities at function definition time

-  Provides hints to resolve ambiguities when they occur

-  Supports namespaces with optional keyword arguments

What this doesn't do
--------------------

-  Vararg dispatch

.. code-block:: python

   @adispatch()
   def add(*args: [int]):
       ...

-  Diagonal dispatch

.. code-block:: python

   a = arbitrary_type()
   @adispatch()
   def are_same_type(x: a, y: a):
       return True


Installation and Dependencies
-----------------------------

``adispatch`` supports Python 3.2+, is pure python and requires no other dependencies.

License
-------

New BSD. See License_.


Links
-----

-  `Five-minute Multimethods in Python by Guido`_
-  `multimethods package on PyPI`_
-  `singledispatch in Python 3.4's functools`_
-  `Clojure Protocols`_
-  `Julia methods docs`_
-  `Karpinksi notebook: *The Design Impact of Multiple Dispatch*`_
-  `Wikipedia article`_
-  `PEP 3124 - *Overloading, Generic Functions, Interfaces, and Adaptation*`_


.. _`Five-minute Multimethods in Python by Guido`:
  http://www.artima.com/weblogs/viewpost.jsp?thread=101605
.. _`multimethods package on PyPI`:
  https://pypi.python.org/pypi/multimethods
.. _`singledispatch in Python 3.4's functools`:
  http://docs.python.org/3.4/library/functools.html#functools.singledispatch
.. _`Clojure Protocols`:
  http://clojure.org/protocols
.. _`Julia methods docs`:
  http://julia.readthedocs.org/en/latest/manual/methods/
.. _`Karpinksi notebook: *The Design Impact of Multiple Dispatch*`:
  http://nbviewer.ipython.org/gist/StefanKarpinski/b8fe9dbb36c1427b9f22
.. _`Wikipedia article`:
  http://en.wikipedia.org/wiki/Multiple_dispatch
.. _`PEP 3124 - *Overloading, Generic Functions, Interfaces, and Adaptation*`:
  http://legacy.python.org/dev/peps/pep-3124/

.. |Build Status| image:: https://travis-ci.org/waipu/adispatch.png
   :target: https://travis-ci.org/waipu/adispatch
.. _License: https://github.com/waipu/adispatch/blob/master/LICENSE
