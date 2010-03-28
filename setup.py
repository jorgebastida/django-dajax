from distutils.core import setup

setup(
    name = "django-dajax",
    version = "0.8.4",
    author = "Benito Jorge Bastida Perez",
    author_email = "jorge@thecodefarm.com",
    description = "Easy to use library to create asynchronous presentation logic with django and dajaxice",
    download_url = "http://cloud.github.com/downloads/jorgebastida/django-dajax/django-dajax-0.8.4.tar.gz",
    url = "http://dajaxproject.com",
    packages=['dajax', 'dajax.core'],
    data_files=[('share/django-dajax', ['src/dojo.dajax.core.js', 'src/jquery.dajax.core.js', 
        'src/mootools.dajax.core.js', 'src/prototype.dajax.core.js'])],
    requires=['dajaxice (>=0.1.2)'],
    classifiers=['Development Status :: 4 - Beta',
                'Environment :: Web Environment',
                'Framework :: Django',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: BSD License',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Topic :: Utilities']
)