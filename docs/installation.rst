Installation
============

In order to use ``dajax`` you should install ``django-dajaxice`` before. Please follow these instructions `here <http://django-dajaxice.readthedocs.org/en/latest/installation.html>`_.

Installing Dajax
----------------

Install ``django-dajax`` using ``easy_install`` or ``pip``::

    $ pip install django_dajax
    $ easy_install django_dajax


Add ``dajax`` in your project settings.py inside ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'dajaxice',
        'dajax',
        ...
    )

Create a new ``ajax.py`` file inside your app with your own dajax functions::

    from dajax.core import Dajax
    def multiply(request, a, b):
        dajax = Dajax()
        result = int(a) * int(b)
        dajax.assign('#result','value',str(result))
        return dajax.json()


Include dajax in your <head>::

Dajax supports up to four JS libraries. You should add to your project base template the one you need.

* `jQuery 1.7.2 <http://jquery.com/>`_ - ``dajax/jquery.core.js``
* `Prototype 1.7 <http://www.prototypejs.org>`_ - ``dajax/prototype.core.js``
* `MooTools 1.4.5 <http://mootools.net/>`_ - ``dajax/mootools.core.js``
* `Dojo 1.7 <http://www.dojotoolkit.org/>`_ - ``dajax/dojo.core.js``

For example for jQuery::

    {% static "dajax/jquery.core.js" %}


Use Dajax
---------

Now you can call your ajax methods using Dajaxice.app.function('Dajax.process')::

    <button onclick="Dajaxice.example.myexample(Dajax.process);">Click here!</button>


The function _Dajax.process_ will process what the server returns and call the appropriate actions.
If you need your own callback, you can change the callback with a function like::

    function my_callback(data){
        Dajax.process(data);
        /* Your js code */
    }

And use it as::

    <button onclick="Dajaxice.app.function(my_callback)">Click here!</button>


