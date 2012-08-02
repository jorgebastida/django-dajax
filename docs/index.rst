django-dajax
============


Dajax is a powerful tool to easily and super-quickly develop asynchronous presentation logic in web applications, using Python and almost no JavaScript source code.

It supports four of the most popular JavaScript frameworks: Prototype, jQuery, Dojo and mootols.

Using ``django-dajaxice`` as communication core, Dajax implements an abstraction layer between presentation logic managed with JavaScript and your Python business logic.

With Dajax you can modify your DOM structure directly from Python.


Documentation
-------------
.. toctree::
   :maxdepth: 2

   installation
   api

   migrating-to-09

   changelog


How does it work?
-----------------

.. image:: img/overview.png


Example
-------

Once you've `installed dajaxice <http://django-dajaxice.readthedocs.org/en/latest/installation.html>`_ and `dajax <http://django-dajax.readthedocs.org/en/latest/installation.html>`_ you can create ajax functions in your Python code::


    from dajax.core import Dajax

    def assign_test(request):
        dajax = Dajax()
        dajax.assign('#box', 'innerHTML', 'Hello World!')
        dajax.add_css_class('div .alert', 'red')
        return dajax.json()


This function will assign to ``#box`` as innerHTML the text ``Hello World!`` and ``Hola!`` to every DOM element that matches ``.btn``.

You can call this function in your html/js code using::

    <div onclick="Dajaxice.app.assign_test(Dajax.process);">Click Here!</div>


Supported JS Frameworks
-----------------------

Dajax currently support four of the most popular:

* `jQuery 1.7.2 <http://jquery.com/>`_
* `Prototype 1.7 <http://www.prototypejs.org>`_
* `MooTools 1.4.5 <http://mootools.net/>`_
* `Dojo 1.7 <http://www.dojotoolkit.org/>`_
