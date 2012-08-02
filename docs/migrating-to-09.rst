Migrating to 0.9
================

Static files
------------

Since ``0.9`` dajax takes advantage of ``django.contrib.staticfiles`` so deploying a dajax application live is much easy than in previous versions.
All the ``X.dajax.core.js`` flavoured files (jQuery, Prototype, ...) are inside a new folder named static instead of src.

You need to remember to run ``python manage.py collectstatic`` before deploying your code live. This command will collect all the static files your application need into ``STATIC_ROOT``. For further information, this is the `Django static files docuemntation <https://docs.djangoproject.com/en/dev/howto/static-files/>`_

You should change all you dajax core imports using for example for jQuery::

    {% static "dajax/jquery.core.js" %}


Imports
-------
If you was importing ``dajax`` using::

    from dajax.core.Dajax import Dajax

you should change it to::

    from dajax.core import Dajax
