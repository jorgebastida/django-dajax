from dajax.core import Dajax
from django.template.loader import render_to_string
from dajaxice.core import dajaxice_functions


def assign_test(request):
    dajax = Dajax()
    dajax.assign('#block01 li','innerHTML','Something else...')
    dajax.append('#console','innerHTML',"dajax.assign('#block01 li','innerHTML','Something else...')<br/>")
    return dajax.json()

dajaxice_functions.register(assign_test)

def clear_test(request):
    dajax = Dajax()
    dajax.clear('#block02 li','innerHTML')
    dajax.append('#console','innerHTML',"dajax.clear('#block02 li','innerHTML')<br/>")
    return dajax.json()

dajaxice_functions.register(clear_test)

def alert_test(request):
    dajax = Dajax()
    dajax.alert('Alert Test Works!!')
    dajax.append('#console','innerHTML',"dajax.alert('Alert Test Works!!')<br/>")
    return dajax.json()

dajaxice_functions.register(alert_test)

def cssadd_test(request):
    dajax = Dajax()
    dajax.add_css_class('#block04 li', 'red')
    dajax.append('#console','innerHTML',"dajax.add_css_class('#block04 li',('red',))<br/>")
    return dajax.json()

dajaxice_functions.register(cssadd_test)

def cssrem_test(request):
    dajax = Dajax()
    dajax.remove_css_class('#block04 li','red')
    dajax.append('#console','innerHTML',"dajax.remove_css_class('#block04 li',('red',))<br/>")
    return dajax.json()

dajaxice_functions.register(cssrem_test)

def append_test(request):
    dajax = Dajax()
    dajax.append('#block06 .row','innerHTML','#')
    dajax.append('#console','innerHTML',"dajax.append('#block06 .row','innerHTML','#')<br/>")
    return dajax.json()

dajaxice_functions.register(append_test)

def prepend_test(request):
    dajax = Dajax()
    dajax.prepend('#block07 .row','innerHTML','#')
    dajax.append('#console','innerHTML',"dajax.prepend('#block07 .row','innerHTML','#')<br/>")
    return dajax.json()

dajaxice_functions.register(prepend_test)

def redirect_test(request):
    dajax = Dajax()
    dajax.redirect('http://djangoproject.com',2000)
    dajax.append('#console','innerHTML',"dajax.redirect('http://djangoproject.com',2000)<br/>")
    return dajax.json()

dajaxice_functions.register(redirect_test)

def script_test(request):
    dajax = Dajax()
    dajax.script('alert("Alert from script!")')
    dajax.append('#console','innerHTML',"dajax.script('alert(\'Alert from script!\')')<br/>")
    return dajax.json()
    
dajaxice_functions.register(script_test)

def remove_test(request):
    dajax = Dajax()
    dajax.remove('#block10 .row')
    dajax.append('#console','innerHTML',"dajax.remove('#block10 .row')<br/>")
    return dajax.json()

dajaxice_functions.register(remove_test)

def adddata_test(request):
    dajax = Dajax()
    dajax.add_data(range(0,10),'my_callback')
    dajax.append('#console','innerHTML',"dajax.add_data(range(0,10),'my_callback')<br/>")
    return dajax.json()

dajaxice_functions.register(adddata_test)

def param_test(request, what):
    dajax = Dajax()
    dajax.alert("You search = %s" % what)
    dajax.append('#console','innerHTML',"dajax.alert(\'You search = %s\' % what)<br/>")
    return dajax.json()

dajaxice_functions.register(param_test)