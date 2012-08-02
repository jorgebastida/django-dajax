API
===

alert(message)
--------------
Alert a ``message``.

* **message**: Any message you want to alert

Usage Example::

    from dajax.core import Dajax

    def alert_example(request):
        dajax = Dajax()
        dajax.alert('Hello from python!')
        return dajax.json()

assign(selector, attribute, value)
----------------------------------
Assign to all elements that matches with the ``selector`` as `attribute`` the ``value``.


* **selector**: CSS selector.
* **attribute**: Any valid attribute.
* **value**: The value you want to assing.

Usage Example::

    from dajax.core import Dajax

    def assign_example(request):
        dajax = Dajax()
        dajax.assign('#button', 'value', 'Click here!')
        dajax.assign('div .alert', 'innerHTML', 'This email is invalid')
        return dajax.json()


add_css_class(selector, value)
------------------------------
Assign to all elements that matches with the ``selector`` the ``CSS`` class ``value``. ``value`` could be a string or a list of them.

* **selector**: CSS selector.
* **value**: Any CSS class name or a list of them.


Usage Example::

    from dajax.core import Dajax

    def add_css_example(request):
        dajax = Dajax()
        dajax.add_css_class('div .alert', 'red')
        dajax.add_css_class('div .warning', ['big', 'yellow'])
        return dajax.json()


remove_css_class(selector, value)
---------------------------------
Remove to all elements that matches with the ``selector`` the ``CSS`` class ``value``. ``value`` could be a string or a list of them.

* **selector**: CSS selector.
* **value**: Any CSS class name or a list of them.


Usage Example::

    from dajax.core import Dajax

    def remove_css_example(request):
        dajax = Dajax()
        dajax.remove_css_class('div .message', 'big-message')
        dajax.remove_css_class('div .total', ['big', 'red'])
        return dajax.json()

append(selector, attribute, value)
----------------------------------

Append to all elements that matches with the ``selector``  ``value`` to with the desired ``attribute``.

* **selector**: CSS selector.
* **attribute**: Any valid attribute.
* **value**: Any CSS class name or a list of them.

Usage Example::

    from dajax.core import Dajax

    def append_example(request):
        dajax = Dajax()
        dajax.assign('#message', 'innerHTML', 'Last message')
        return dajax.json()


prepend(selector, attribute, value)
-----------------------------------

Prepend to all elements that matches with the ``selector`` ``value`` to with the desired ``attribute``.

* **selector**: CSS selector.
* **attribute**: Any valid attribute.
* **value**: Any CSS class name or a list of them.

Usage Example::

    from dajax.core import Dajax

    def prepend_example(request):
        dajax = Dajax()
        dajax.prepend('#message', 'innerHTML', 'First message')
        return dajax.json()


clear(selector, attribute)
--------------------------

Clear all elements that matches with the ``selector`` the  desired ``attribute``.

* **selector**: CSS selector.
* **attribute**: Any valid attribute.

Usage Example::

    from dajax.core import Dajax

    def clear_example(request):
        dajax = Dajax()
        dajax.clear('#message', 'innerHTML')
        return dajax.json()


redirect(url, delay=0)
----------------------

Redirect current page to ``url`` with a delay of ``ms``.

* **url**: Destination URL.
* **delay**: Number of ms that the browser should wait before redirecting.

Usage Example::

    from dajax.core import Dajax

    def redirect_example(request):
        dajax = Dajax()
        dajax.redirect('http://google.com', delay=2000)
        return dajax.json()


script(code)
------------

Executes ``code`` in the browser

* **code**: Code to execute.

Usage Example::

    from dajax.core import Dajax

    def code_example(request):
        dajax = Dajax()
        dajax.code('my_function();')
        return dajax.json()


remove(selector)
----------------

Remove all elements that matches ``selector``.

* **selector**: CSS selector.

Usage Example::

    from dajax.core import Dajax

    def code_example(request):
        dajax = Dajax()
        dajax.remove('.message')
        return dajax.json()


add_data(data, callback_function)
---------------------------------

Send ``data`` to the browser and call ``callback_function`` using this ``data``.

* **data**: Data you want to send to your function.
* **callback_function**: Fuction you want to call in the browser.

Usage Example::

    from dajax.core import Dajax

    def data_example(request):
        dajax = Dajax()
        dajax.add_data(range(10), 'my_js_function')
        return dajax.json()
