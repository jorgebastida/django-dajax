django-dajax
============

Dajax is a powerfull tool to easily and super-fastly develop asynchronous presentation logic in web applications using python and almost no lines of JS source code.

It supports up to four of the most popular JS frameworks:

* jQuery
* Prototype
* Dojo
* mootols

Using ``django-dajaxice`` communication core, ``django-dajax`` implements an abstraction layer between the presentation logic managed with JS and your python business logic. With dajax you can modify your ``DOM`` structure directly from python.

For more information about how django-dajax works: https://dajaxproject.com

Official site http://dajaxproject.com
Documentation http://readthedocs.org/projects/django-dajax/

Project status
----------------
From ``v0.9.2`` this project is not going to accept new features. In order to not break existing projects using this library, ``django-dajax`` and ``django-dajaxice`` will be maintained until ``django 1.8`` is released.


Should I use django-dajax or django-dajaxice?
---------------------------------------------
In a word, No. I created these projects 4 years ago as a cool tool in order to solve one specific problems I had at that time.

These days using these projects is a bad idea.

Perhaps I'm more pragmatic now, perhaps my vision of how my django projects should be coupled to libraries like these has change, or perhaps these days I really treasure the purity and simplicity of a vanilla django development.

If you want to use this project, you are probably wrong. You should stop couplig your interface with your backend or... in the long term it will explode in your face.

Forget about adding more unnecessary complexity. Keep things simple.
